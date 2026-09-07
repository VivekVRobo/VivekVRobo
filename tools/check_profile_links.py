from __future__ import annotations

import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

OWNER = "VivekVRobo"
EXPECTED_REPOSITORIES = {
    "slam-robot-ros2",
    "robotic-character-interface",
    "3dof-robotic-arm",
    "custom-pcb-motor-driver",
    "http-server-from-scratch",
    "Aurelia-Chan-Source",
    "line-following-robot",
    "cv-object-sorter",
    "gesture-controlled-robot",
}


def linked_repositories(readme: str) -> set[str]:
    pattern = rf"https://github\.com/{re.escape(OWNER)}/([A-Za-z0-9_.-]+)"
    return set(re.findall(pattern, readme))


def repository_exists(name: str, token: str | None) -> bool:
    request = urllib.request.Request(
        f"https://api.github.com/repos/{OWNER}/{name}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "VivekVRobo-profile-integrity",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return response.status == 200
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
        return False


def main() -> int:
    readme_path = Path("README.md")
    if not readme_path.is_file():
        print("README.md is missing", file=sys.stderr)
        return 1

    linked = linked_repositories(readme_path.read_text(encoding="utf-8"))
    missing_from_profile = sorted(EXPECTED_REPOSITORIES - linked)
    unexpected = sorted(linked - EXPECTED_REPOSITORIES)

    if missing_from_profile:
        print(f"Expected profile repository links are missing: {missing_from_profile}", file=sys.stderr)
        return 1

    if unexpected:
        print(f"Update EXPECTED_REPOSITORIES for new portfolio links: {unexpected}", file=sys.stderr)
        return 1

    token = os.getenv("GITHUB_TOKEN")
    unavailable = sorted(name for name in linked if not repository_exists(name, token))
    if unavailable:
        print(f"Linked repositories could not be resolved through the GitHub API: {unavailable}", file=sys.stderr)
        return 1

    print(f"Profile integrity OK: {len(linked)} portfolio repositories linked and resolvable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
