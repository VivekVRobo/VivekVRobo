from __future__ import annotations

import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

OWNER = "VivekVRobo"

EXPECTED_REPOSITORIES = {
    "gesture-controlled-robotic-arm",
    "slam-robot-ros2",
    "universal-brain",
}

REQUIRED_EXTERNAL_LINKS = {
    "https://github.com/manankharwar/fusioncore",
    "https://github.com/manankharwar/fusioncore/issues/81",
    "https://github.com/manankharwar/fusioncore/pull/96",
}

REQUIRED_LOCAL_ASSETS = {
    "assets/vivek-robotics-slam.svg",
    "assets/slam-benchmark-pipeline.svg",
    "assets/universal-brain-architecture.svg",
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

    readme = readme_path.read_text(encoding="utf-8")
    linked = linked_repositories(readme)

    missing_from_profile = sorted(EXPECTED_REPOSITORIES - linked)
    unexpected = sorted(linked - EXPECTED_REPOSITORIES)

    if missing_from_profile:
        print(f"Expected featured repository links are missing: {missing_from_profile}", file=sys.stderr)
        return 1

    if unexpected:
        print(
            "Update EXPECTED_REPOSITORIES if a new first-party repository is intentionally featured: "
            f"{unexpected}",
            file=sys.stderr,
        )
        return 1

    missing_external = sorted(url for url in REQUIRED_EXTERNAL_LINKS if url not in readme)
    if missing_external:
        print(f"Required upstream evidence links are missing: {missing_external}", file=sys.stderr)
        return 1

    missing_assets = sorted(path for path in REQUIRED_LOCAL_ASSETS if not Path(path).is_file())
    if missing_assets:
        print(f"Required profile assets are missing: {missing_assets}", file=sys.stderr)
        return 1

    token = os.getenv("GITHUB_TOKEN")
    unavailable = sorted(name for name in linked if not repository_exists(name, token))
    if unavailable:
        print(f"Featured repositories could not be resolved through the GitHub API: {unavailable}", file=sys.stderr)
        return 1

    print(
        "Profile integrity OK: "
        f"{len(linked)} featured repositories, "
        f"{len(REQUIRED_EXTERNAL_LINKS)} upstream evidence links, and "
        f"{len(REQUIRED_LOCAL_ASSETS)} local assets validated."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
