<div align="center">

# Vivek Vala

### Robotics & Autonomous Systems · Embodied AI · Systems Engineering

I build **robots, autonomy systems, intelligent runtimes, and low-level engineering projects** with an emphasis on measurable results, reproducibility, and explicit evidence.

[**Portfolio**](https://vivek-vala-portfolio.vercel.app/) · [**Start with the robotic arm**](https://github.com/VivekVRobo/gesture-controlled-robotic-arm) · [**Explore SLAM**](https://github.com/VivekVRobo/slam-robot-ros2)

**Follow this profile for robotics builds, engineering experiments, benchmarks, and open-source systems.**

</div>

---

## Start here

<table>
<tr>
<td width="33%" valign="top">

### 🤖 Gesture-Controlled Robotic Arm
**Physical robotics**

Wearable MPU6050 gesture control over nRF24L01, driving a multi-joint robotic arm with real hardware actuation evidence.

**Stack:** Arduino · C++ · MPU6050 · nRF24L01 · PCA9685

[Repository →](https://github.com/VivekVRobo/gesture-controlled-robotic-arm)

</td>
<td width="33%" valign="top">

### 🗺️ ROS 2 SLAM Robot
**Autonomy & localization**

Reproducibility-first 2D LiDAR SLAM with Gazebo ground truth, ATE/RPE evaluation, loop-closure metrics, and rosbag regression.

**Stack:** ROS 2 · Gazebo · LiDAR · Python · SLAM Toolbox

[Repository →](https://github.com/VivekVRobo/slam-robot-ros2)

</td>
<td width="33%" valign="top">

### 🧠 Universal Brain
**Intelligent systems**

Local-first multi-model executive architecture with authority boundaries, durable missions, model routing, recovery, and verification.

**Stack:** Python · local models · orchestration · security · systems architecture

[Repository →](https://github.com/VivekVRobo/universal-brain)

</td>
</tr>
</table>

---

## What I build

```text
Physical Robotics
      ↓
Perception + SLAM
      ↓
Planning + Control
      ↓
Embedded Electronics
      ↓
Systems Engineering
      ↓
Intelligent Runtime Architecture
```

My repositories are meant to demonstrate different layers of the same engineering direction: **building systems that sense, reason, act, recover, and can be measured honestly**.

---

## Flagship engineering work

| Project | Engineering focus | Evidence status |
| --- | --- | --- |
| **[gesture-controlled-robotic-arm](https://github.com/VivekVRobo/gesture-controlled-robotic-arm)** | Wireless wearable control, sensor fusion, RF telemetry, servo actuation | Physical hardware demo and bench evidence published |
| **[slam-robot-ros2](https://github.com/VivekVRobo/slam-robot-ros2)** | ROS 2 SLAM, Gazebo ground truth, ATE/RPE, loop closure, rosbag regression | Static contracts + ROS build CI verified; runtime benchmark evidence still gated |
| **[3dof-robotic-arm](https://github.com/VivekVRobo/3dof-robotic-arm)** | Analytic FK/IK, Cartesian planning, workspace/Jacobian analysis, Arduino control | Numerical/software validation in CI; physical accuracy evidence pending |
| **[custom-pcb-motor-driver](https://github.com/VivekVRobo/custom-pcb-motor-driver)** | DRV8848 motor-driver PCB, current/thermal modeling, KiCad workflow | Analytical design evidence in CI; fabrication/bench evidence pending |
| **[http-server-from-scratch](https://github.com/VivekVRobo/http-server-from-scratch)** | C++20 HTTP/1.1 from raw sockets, secure static files, bounded concurrency, Linux epoll | Linux + Windows CI verified; controlled performance campaign pending |
| **[universal-brain](https://github.com/VivekVRobo/universal-brain)** | Local-first executive runtime, permissions, durable missions, multi-model routing, verification | Engineering checkpoints verified; target-machine endurance evidence still in progress |

---

## More robotics projects

- **[robotic-character-interface](https://github.com/VivekVRobo/robotic-character-interface)** — safety-governed embodied AI, motion authorization, digital twin, telemetry, and fault testing.
- **[line-following-robot](https://github.com/VivekVRobo/line-following-robot)** — control stack, PID behavior, regression testing, and robustness sweeps.
- **[cv-object-sorter](https://github.com/VivekVRobo/cv-object-sorter)** — OpenCV perception → decision → actuation pipeline with evaluation tooling.
- **[gesture-controlled-robot](https://github.com/VivekVRobo/gesture-controlled-robot)** — MediaPipe gesture control with temporal stabilization, STOP fail-safe, heartbeat, and watchdog behavior.

---

## Engineering stack

| Area | Technologies |
| --- | --- |
| **Robotics** | ROS 2, SLAM, Gazebo, TF, localization, kinematics, trajectory evaluation |
| **Computer vision** | OpenCV, MediaPipe, HSV/contour pipelines, offline evaluation |
| **Embedded systems** | Arduino, servo control, PCA9685, serial protocols, watchdogs |
| **Electronics** | KiCad, PCB design workflow, motor drivers, current/thermal modeling |
| **Systems** | C++20, raw sockets, HTTP/1.1, Linux epoll, concurrency, benchmarking |
| **Software** | Python, FastAPI, Flask, SQLite, React, TypeScript, automated testing |
| **Engineering workflow** | Git, GitHub Actions, CI, machine-readable evidence, reproducible runbooks |

---

## Current build log

I am currently pushing several projects from **implemented** to **measured**:

- **SLAM:** publish the first genuine Gazebo benchmark evidence bundle.
- **3-DOF arm:** add real endpoint-accuracy and repeatability measurements.
- **Motor-driver PCB:** progress from analytical/CAD validation to fabrication and bench evidence.
- **Universal Brain:** execute real-environment Windows/WSL2/Ollama validation and endurance runs.
- **Systems work:** publish reproducible performance evidence for the C++ HTTP server.

This is where new results, failures, benchmarks, and lessons will appear.

---

<details>
<summary><strong>Engineering principles</strong></summary>

### Measure before claiming

Simulation results stay simulation results. Analytical results stay analytical results. Physical claims require physical evidence.

### Reproducibility over screenshots

Important experiments should preserve the **exact commit, environment, configuration, raw artifacts, metrics, and failure cases** so another developer can reproduce or challenge the result.

### Deterministic safety around actuation

AI, perception, UI, and character layers should not directly command physical actuators. Motion authority belongs behind explicit planning, validation, safety supervision, and hardware boundaries.

### Build systems that can be inspected

Architecture, failure modes, limitations, evidence maturity, and release gates are treated as part of the engineering, not as afterthoughts.

</details>

---

## Collaborate

If you work on **robotics, ROS 2, SLAM, embedded control, computer vision, autonomous systems, or systems engineering**, useful issues, experiments, benchmark reproductions, and technical discussions are welcome across the repositories.

**Primary direction:** robotics systems that are measurable, reproducible, safety-conscious, and explicit about what has actually been demonstrated.
