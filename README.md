<img align="right" src="./assets/vivek-robotics-slam.svg" width="48%" alt="Animated robotics workspace with robotic arm, LiDAR, SLAM trajectories and embedded control" />

# Vivek Vala

### Robotics · Autonomous Systems · Embedded Intelligence

Building physical robots and autonomous systems where claims are backed by **code, measurements, and real hardware**.

Focused on **SLAM, robotic manipulation, embedded autonomy, and reliable autonomous systems**.

**Evidence over hype.**

[**Portfolio**](https://vivek-vala-portfolio.vercel.app/) · [**Contact**](https://vivek-vala-portfolio.vercel.app/#contact) · [**Open Source**](https://github.com/manankharwar/fusioncore/pull/96)

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

**Evidence:** Physical actuation ✅ · Firmware verification ✅ · Latency and repeatability ◐ Pending

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

**Evidence:** Package and CI contracts ✅ · Benchmark tooling ✅ · Published runtime ATE / RPE ◐ Pending

[**Repository →**](https://github.com/VivekVRobo/slam-robot-ros2) · [**Benchmark runbook →**](https://github.com/VivekVRobo/slam-robot-ros2/blob/main/docs/BENCHMARK_EVIDENCE_RUNBOOK.md) · [**Trajectory evaluator →**](https://github.com/VivekVRobo/slam-robot-ros2/blob/main/tools/trajectory_metrics.py) · [**Release gate →**](https://github.com/VivekVRobo/slam-robot-ros2/blob/main/docs/RELEASE_READINESS.md)

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
| **ROS 2 SLAM** | Package contracts, evaluation and benchmark tooling ✅ | Runtime ATE / RPE evidence still pending |
| **Universal Brain** | V5.3 verification record and cross platform validation harness ✅ | Windows / WSL2 target endurance still pending |
| **Open Source** | FusionCore PR #96 merged upstream ✅ | New entries only after upstream acceptance |

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

> Future contributions appear here only after they are accepted upstream.

---

## Engineering Stack

### Robotics

<img src="https://img.shields.io/badge/ROS_2-425866?style=flat-square&logo=ros&logoColor=white" alt="ROS 2"> <img src="https://img.shields.io/badge/Gazebo-425866?style=flat-square&logo=gazebo&logoColor=white" alt="Gazebo"> <img src="https://img.shields.io/badge/SLAM-425866?style=flat-square" alt="SLAM"> <img src="https://img.shields.io/badge/Nav2-425866?style=flat-square" alt="Nav2"> <img src="https://img.shields.io/badge/MoveIt_2-425866?style=flat-square" alt="MoveIt 2">

### Embedded

<img src="https://img.shields.io/badge/C-425866?style=flat-square&logo=c&logoColor=white" alt="C"> <img src="https://img.shields.io/badge/C++-425866?style=flat-square&logo=cplusplus&logoColor=white" alt="C++"> <img src="https://img.shields.io/badge/Arduino-425866?style=flat-square&logo=arduino&logoColor=white" alt="Arduino"> <img src="https://img.shields.io/badge/STM32-425866?style=flat-square&logo=stmicroelectronics&logoColor=white" alt="STM32"> <img src="https://img.shields.io/badge/PCA9685-425866?style=flat-square" alt="PCA9685">

### Perception

<img src="https://img.shields.io/badge/OpenCV-425866?style=flat-square&logo=opencv&logoColor=white" alt="OpenCV"> <img src="https://img.shields.io/badge/MediaPipe-425866?style=flat-square" alt="MediaPipe"> <img src="https://img.shields.io/badge/LiDAR-425866?style=flat-square" alt="LiDAR"> <img src="https://img.shields.io/badge/Sensor_Fusion-425866?style=flat-square" alt="Sensor Fusion">

### Systems

<img src="https://img.shields.io/badge/Linux-425866?style=flat-square&logo=linux&logoColor=white" alt="Linux"> <img src="https://img.shields.io/badge/Git-425866?style=flat-square&logo=git&logoColor=white" alt="Git"> <img src="https://img.shields.io/badge/CMake-425866?style=flat-square&logo=cmake&logoColor=white" alt="CMake"> <img src="https://img.shields.io/badge/GitHub_Actions-425866?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions"> <img src="https://img.shields.io/badge/Networking-425866?style=flat-square" alt="Networking">

### Intelligence

<img src="https://img.shields.io/badge/Python-425866?style=flat-square&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/Local_LLMs-425866?style=flat-square" alt="Local LLMs"> <img src="https://img.shields.io/badge/Agent_Systems-425866?style=flat-square" alt="Agent Systems"> <img src="https://img.shields.io/badge/Tool_Execution-425866?style=flat-square" alt="Tool Execution">

---

## Research / Systems Interests

`ROS 2` · `SLAM` · `Localization` · `Controls` · `Embedded Robotics` · `Computer Vision` · `Sensor Fusion` · `Physical AI` · `Autonomous Agents` · `Reliable Systems`

---

## GitHub Activity

<p align="center">
  <img src="https://ghchart.rshah.org/6F90A8/VivekVRobo" alt="VivekVRobo GitHub contribution activity" width="92%" />
</p>

The activity graph is secondary to the engineering evidence above. Projects, accepted upstream work, tests, measurements, and real hardware remain the primary signals.

---

## Building / Research / Collaboration

I am interested in work across `Robotics`, `ROS 2`, `Autonomy`, `Embedded Systems`, `Controls`, `Computer Vision`, `Physical AI`, and `Systems Engineering`.

<p align="center">
  <a href="https://vivek-vala-portfolio.vercel.app/"><strong>Portfolio</strong></a> ·
  <a href="https://github.com/VivekVRobo?tab=repositories"><strong>Projects</strong></a> ·
  <a href="https://github.com/manankharwar/fusioncore/pull/96"><strong>Open Source</strong></a> ·
  <a href="https://vivek-vala-portfolio.vercel.app/#contact"><strong>Contact</strong></a>
</p>

<p align="center"><strong>Build · Measure · Verify · Improve</strong></p>
