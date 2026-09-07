# Final GitHub UI Setup Checklist

This file contains the small set of profile/repository actions that cannot currently be changed through the connected GitHub automation. Everything here is intentionally UI-only.

## 1. Profile bio

Set the GitHub profile bio to:

> Robotics & Automation | ROS 2 • SLAM • Computer Vision • Embedded Systems • C++/Python

## 2. Pin these six repositories in this exact order

1. `slam-robot-ros2`
2. `robotic-character-interface`
3. `3dof-robotic-arm`
4. `custom-pcb-motor-driver`
5. `http-server-from-scratch`
6. `Aurelia-Chan-Source`

The intended portfolio narrative is:

`autonomy → safety-governed embodiment → manipulation → electronics → low-level systems → cognitive runtime`

## 3. Repository descriptions and topics

### slam-robot-ros2

**Description**

> Reproducibility-first ROS 2 SLAM benchmark with Gazebo ground truth, ATE/RPE, loop-closure metrics, rosbag regression, and evidence gates.

**Topics**

`ros2` `slam` `robotics` `gazebo` `lidar` `localization` `slam-toolbox` `rosbag` `autonomous-navigation` `benchmarking`

### robotic-character-interface

**Description**

> Safety-governed multimodal character embodiment platform with deterministic planning, motion authorization, firmware contracts, digital-twin telemetry, and fault evidence.

**Topics**

`robotics` `embodied-ai` `human-robot-interaction` `digital-twin` `robot-safety` `fastapi` `react` `firmware` `python` `cpp`

### 3dof-robotic-arm

**Description**

> 3-DOF robotic arm with analytic FK/IK, Cartesian planning, servo calibration, Arduino control, numerical workspace analysis, and physical-validation tooling.

**Topics**

`robotics` `robotic-arm` `inverse-kinematics` `forward-kinematics` `kinematics` `arduino` `servo` `pca9685` `python` `embedded-systems`

### custom-pcb-motor-driver

**Description**

> Evidence-gated DRV8848 dual brushed-DC motor-driver PCB with KiCad capture, tolerance-aware current/thermal modeling, validation gates, and CI.

**Topics**

`pcb` `kicad` `motor-driver` `drv8848` `electronics` `robotics` `hardware` `power-electronics` `embedded-systems` `ci`

### http-server-from-scratch

**Description**

> C++20 HTTP/1.1 server from raw sockets with incremental parsing, secure static files, bounded thread pool, Linux epoll, adversarial tests, and reproducible benchmarks.

**Topics**

`cpp` `cpp20` `http` `http-server` `networking` `sockets` `epoll` `systems-programming` `web-server` `benchmarking`

### Aurelia-Chan-Source

**Description**

> Experimental cognitive runtime with DAG execution, durable persistence, verification contracts, persona rendering, deterministic evidence, and an actuator-free embodiment boundary.

**Topics**

`ai-agents` `cognitive-architecture` `agent-runtime` `python` `flask` `sqlite` `dag` `persistence` `embodied-ai` `human-robot-interaction`

## 4. Create first GitHub Releases

The automation connection can read releases but cannot create release pages or version tags. Copy-ready release-note drafts and release gates are already committed in each repository.

### slam-robot-ros2

- Tag: `v0.1.0`
- Title: `v0.1.0 — Reproducible ROS 2 SLAM Engineering Reference`
- Copy/adapt: `docs/RELEASE_NOTES_DRAFT.md`
- Check first: `docs/RELEASE_READINESS.md`
- Do not claim a successful Gazebo benchmark until a genuine runtime evidence bundle exists.

### robotic-character-interface

- Tag: `v0.1.0`
- Title: `v0.1.0 — Safety-Governed Robotic Character Interface (Simulation Release)`
- Copy/adapt: `docs/RELEASE_NOTES_DRAFT.md`
- Check first: `docs/RELEASE_CHECKLIST.md`
- Keep physical-hardware validation explicitly pending.

### http-server-from-scratch

- Tag: `v0.1.0`
- Title: `v0.1.0 — C++20 HTTP/1.1 Server Engineering Reference`
- Copy/adapt: `docs/RELEASE_NOTES_DRAFT.md`
- Check first: `docs/RELEASE_READINESS.md`
- Do not claim a threadpool/epoll winner until controlled-host M6B.2 evidence exists.

### Aurelia-Chan-Source

Release preparation is complete: package metadata is `0.6.0`, the README/readiness docs are aligned, the release candidate passed all four validation jobs plus deterministic cognitive-cycle evidence, and the post-merge `main` validation run also passed on commit `faa8f476fb5e23cc3df3fd7fd34dd1563c3ba2ed`.

- Tag: `v0.6.0`
- Title: `v0.6.0 — Deterministic Cognitive Runtime Evidence Release`
- Copy/adapt: `docs/RELEASE_NOTES_DRAFT.md`
- Check first: `docs/RELEASE_READINESS.md`

## 5. Visual proof policy

Do not upload generated or borrowed imagery as engineering evidence.

Add visuals only when they come from the actual project execution or hardware:

- SLAM: real Gazebo/map/trajectory/metrics capture from the repository.
- RCI: actual dashboard + digital-twin telemetry capture.
- vhttp: real controlled benchmark/report once M6B.2 is executed.
- 3-DOF arm: real CAD/assembled arm/physical measurement evidence when available.
- PCB: actual KiCad schematic/layout/3D render now; fabricated-board and bench media only after fabrication.
- Aurelia: actual browser/runtime UI and deterministic evidence artifacts.

## 6. Completion definition

This UI phase is complete when:

- [ ] profile bio is updated;
- [ ] six repositories are pinned in the specified order;
- [ ] all six descriptions are updated;
- [ ] all six topic sets are applied;
- [ ] SLAM `v0.1.0` release exists;
- [ ] RCI `v0.1.0` release exists;
- [ ] vhttp `v0.1.0` release exists;
- [ ] Aurelia `v0.6.0` release exists;
- [ ] no unsupported hardware/performance/AGI claims were introduced while doing so.
