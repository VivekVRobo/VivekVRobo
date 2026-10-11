<img align="right" src="./assets/vivek-robotics-slam.svg" width="48%" alt="Animated robotics workspace with robotic arm, LiDAR, SLAM trajectories and embedded control" />

# Vivek Vala

### Robotics · Autonomous Systems · Embedded Intelligence

Building physical robots and autonomous systems where claims are backed by **code, measurements, and real hardware**.

Focused on **SLAM, robotic manipulation, embedded autonomy, and reliable autonomous systems**.

**Evidence over hype.**

[**Portfolio**](https://vivek-vala-portfolio.vercel.app/) · [**Contact**](https://vivek-vala-portfolio.vercel.app/#contact) · [**Open Source**](#open-source)

<br clear="right" />

---

## Current Work

**ROS 2 / SLAM**  
Ground truth benchmarking, trajectory evaluation, loop closure analysis, and reproducible evidence.

**Robotic Manipulation**  
Physical control, calibration, gesture teleoperation, endpoint accuracy, and repeatability.

**Autonomous Systems**  
Durable execution, explicit authority, recovery, verification, and local first orchestration.

**Open Source**  
Focused upstream contributions where the work can be reviewed, tested, and accepted.

---

## Featured Engineering

Three systems, one standard: **implementation, measurable evidence, and explicit proof boundaries.**

### 01 · Gesture Controlled Robotic Arm

<p align="center">
  <a href="https://github.com/VivekVRobo/gesture-controlled-robotic-arm">
    <img src="https://raw.githubusercontent.com/VivekVRobo/gesture-controlled-robotic-arm/main/docs/images/arm-and-glove.png" alt="Gesture controlled robotic arm and wearable control glove" width="88%" />
  </a>
</p>

**Wearable IMU control over 2.4 GHz RF driving a physical multi joint robotic arm.**

`C++` · `Arduino` · `MPU6050` · `nRF24L01` · `PCA9685`

**Evidence:** Physical actuation ✅ · Firmware verification ✅ · Latency and repeatability ✅

[**Repository →**](https://github.com/VivekVRobo/gesture-controlled-robotic-arm) · [**Actuation video →**](https://github.com/VivekVRobo/gesture-controlled-robotic-arm/blob/main/docs/media/physical_actuation_evidence.mp4) · [**Hardware bench →**](https://github.com/VivekVRobo/gesture-controlled-robotic-arm/blob/main/docs/images/robotic_arm_hardware_bench.jpg) · [**Verification tests →**](https://github.com/VivekVRobo/gesture-controlled-robotic-arm/blob/main/tests/test_firmware_motion_engine.py)

---

### 02 · ROS 2 SLAM Benchmarking

<p align="center">
  <a href="https://github.com/VivekVRobo/slam-robot-ros2">
    <img src="./assets/slam-benchmark-pipeline.svg" alt="ROS 2 SLAM ground truth benchmark pipeline" width="88%" />
  </a>
</p>

**A reproducibility first SLAM stack that evaluates estimated motion against independent Gazebo ground truth.**

`ROS 2` · `Gazebo` · `LiDAR` · `SLAM Toolbox` · `ATE` · `RPE`

**Evidence:** Package and CI contracts ✅ · [Verified Gazebo simulation metrics ✅](https://github.com/VivekVRobo/slam-robot-ros2/blob/main/evidence/reports/gazebo-2026-09-17-ec9ceb2e.md) · Replay and hardware validation ◐ Pending

[**Repository →**](https://github.com/VivekVRobo/slam-robot-ros2) · [**Measured Gazebo evidence →**](https://github.com/VivekVRobo/slam-robot-ros2/blob/main/evidence/reports/gazebo-2026-09-17-ec9ceb2e.md) · [**Benchmark runbook →**](https://github.com/VivekVRobo/slam-robot-ros2/blob/main/docs/BENCHMARK_EVIDENCE_RUNBOOK.md) · [**Trajectory evaluator →**](https://github.com/VivekVRobo/slam-robot-ros2/blob/main/tools/trajectory_metrics.py) · [**Release gate →**](https://github.com/VivekVRobo/slam-robot-ros2/blob/main/docs/RELEASE_READINESS.md)

---

### 03 · Universal Brain

<p align="center">
  <a href="https://github.com/VivekVRobo/universal-brain">
    <img src="./assets/universal-brain-architecture.svg" alt="Universal Brain deterministic control plane architecture" width="88%" />
  </a>
</p>

**A local first autonomous execution system that separates model reasoning from persistent authority, state, recovery, and verification.**

`Python` · `Model Routing` · `Durable Missions` · `Authority Gates` · `Verification`

**Evidence:** V5.3 verification record ✅ · Cross platform evidence harness ✅ · Windows / WSL2 target proof ◐ Pending

[**Repository →**](https://github.com/VivekVRobo/universal-brain) · [**Architecture →**](https://github.com/VivekVRobo/universal-brain/blob/main/docs/architecture/SYSTEM_ARCHITECTURE.md) · [**Verification record →**](https://github.com/VivekVRobo/universal-brain/blob/main/docs/testing/ENGINEERING_AGENCY_V53_VERIFICATION.md) · [**Threat model →**](https://github.com/VivekVRobo/universal-brain/blob/main/docs/security/THREAT_MODEL.md)

---

## Proof Ledger

A compact view of what is **verified now** and what is still explicitly gated.

| System | Current proof | Boundary |
| --- | --- | --- |
| **Robotic Arm** | Physical actuation, hardware bench, firmware tests ✅ | Latency and repeatability still need measurement |
| **ROS 2 SLAM** | Successful Gazebo benchmark and archived ATE/RPE results ✅ | Rosbag replay, current-main reproduction and hardware pending |
| **Universal Brain** | V5.3 verification record and cross platform validation harness ✅ | Windows / WSL2 target endurance still pending |
| **Open Source** | FusionCore #96 and Prefect #23352 merged upstream ✅ | Other PRs remain pending maintainer review |

---

## Open Source

### FusionCore · PR #96 · Merged Upstream ✅

**ROS 2 GNSS frame resolution and TF validation**

I fixed a real frame mismatch in FusionCore where GNSS validation could assume `gnss_link` even when a driver published another frame such as `gps`.

**What changed**

- added configurable `gnss.frame_id` support
- resolved the active GNSS frame as **configured override → message header → `gnss_link` fallback**
- used the resolved frame for TF validation and NavSatFix lever arm lookup
- added focused regression coverage for override, message, and fallback precedence
- kept the change scoped to the reported GNSS frame issue

**Upstream result:** merged **September 8, 2026** · 5 files changed · accepted into the original FusionCore repository

[**View merged PR #96 →**](https://github.com/manankharwar/fusioncore/pull/96) · [**Original issue #81 →**](https://github.com/manankharwar/fusioncore/issues/81) · [**FusionCore repository →**](https://github.com/manankharwar/fusioncore)

### Prefect · PR #23352 · Merged Upstream ✅

**Flow-run activity chart navigation**

Fixed the production flow-run activity chart so populated bars provide native, accessible links to the corresponding flow runs. Empty bars remain non-interactive, and regression tests cover click and keyboard navigation without conflicting parent-row behavior.

**Upstream result:** merged **October 9, 2026 (UTC)** after maintainer approval and successful UI checks.

[**View merged PR #23352 →**](https://github.com/PrefectHQ/prefect/pull/23352) · [**Prefect repository →**](https://github.com/PrefectHQ/prefect)

> Future contributions appear here only after they are accepted upstream.

---

## Engineering Stack

| Capability | Evidence based stack |
| --- | --- |
| **Robotics & SLAM** | ROS 2 · Gazebo · SLAM Toolbox · LiDAR · TF frames · ATE / RPE · rosbag regression |
| **Embedded Control** | C++ · Arduino · MPU6050 · nRF24L01 · PCA9685 · servo motion control |
| **Autonomous Systems** | Python · FastAPI · model routing · durable missions · authority gates · recovery · verification |
| **Engineering Infrastructure** | Git · CMake · GitHub Actions · automated tests · benchmarking · evidence driven validation |

The emphasis is on technologies used in implemented systems, not an exhaustive list of tools I have touched.

---

## Research Directions

**State Estimation & SLAM**  
Localization, loop closure, trajectory evaluation, and reproducible benchmarking.

**Robot Manipulation & Control**  
Calibration, teleoperation, bounded motion, endpoint accuracy, and repeatability.

**Embedded Autonomy**  
Sensor fusion, RF control, actuator safety, and hardware backed verification.

**Reliable Autonomous Systems**  
Authority, recovery, verification, durable execution, and evidence based completion.

[**Repositories →**](https://github.com/VivekVRobo?tab=repositories) · [**Contribution history →**](https://github.com/VivekVRobo?tab=overview&from=2026-01-01&to=2026-12-31) · [**Merged FusionCore #96 →**](https://github.com/manankharwar/fusioncore/pull/96) · [**Merged Prefect #23352 →**](https://github.com/PrefectHQ/prefect/pull/23352)

---

## Connect

Open to serious work in robotics, autonomous systems, embedded control, and reliable AI systems.

<p align="center">
  <a href="https://vivek-vala-portfolio.vercel.app/#contact"><strong>Contact</strong></a> ·
  <a href="https://github.com/VivekVRobo"><strong>GitHub</strong></a>
</p>

<p align="center"><strong>Build · Measure · Verify · Improve</strong></p>
