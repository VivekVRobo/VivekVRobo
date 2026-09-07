<div align="center">

# Vivek Vala

### Robotics & Autonomous Systems · Embodied AI · Systems Engineering

I build **measurable robotics and engineering systems** across SLAM, robot control, manipulation, computer vision, embedded electronics, and low-level systems.

My projects emphasize **reproducibility, deterministic testing, explicit safety boundaries, and a strict separation between software/simulation evidence and physical hardware validation**.

</div>

---

## Flagship engineering work

| Project | Engineering focus | Evidence status |
| --- | --- | --- |
| **[slam-robot-ros2](https://github.com/VivekVRobo/slam-robot-ros2)** | ROS 2 SLAM, Gazebo ground truth, ATE/RPE, loop closure, rosbag regression, resource profiling | Static contracts + ROS Lyrical build CI verified; live Gazebo benchmark and hardware evidence remain gated |
| **[robotic-character-interface](https://github.com/VivekVRobo/robotic-character-interface)** | Safety-governed embodied AI, motion authorization, firmware contracts, digital twin, telemetry, adversarial fault testing | Software-complete and simulation-validated; physical HIL validation pending |
| **[3dof-robotic-arm](https://github.com/VivekVRobo/3dof-robotic-arm)** | Analytic FK/IK, Cartesian planning, workspace/Jacobian analysis, servo calibration, Arduino control | Numerical/software validation in CI; physical endpoint accuracy pending |
| **[custom-pcb-motor-driver](https://github.com/VivekVRobo/custom-pcb-motor-driver)** | DRV8848 dual motor-driver PCB, tolerance-aware current/thermal modeling, KiCad workflow, evidence gates | Analytical design evidence in CI; CAD/fabrication/bench evidence remain gated |
| **[http-server-from-scratch](https://github.com/VivekVRobo/http-server-from-scratch)** | C++20 HTTP/1.1 from raw sockets, secure static files, bounded concurrency, Linux `epoll`, reproducible benchmarks | Linux + Windows CI verified; controlled-host M6B.2 performance evidence pending |
| **[Aurelia-Chan-Source](https://github.com/VivekVRobo/Aurelia-Chan-Source)** | Cognitive runtime, DAG execution, durable persistence, verification contracts, persona/embodiment boundary | Deterministic five-run cognitive-cycle evidence in CI; production-scale and physical embodiment claims remain gated |

### The portfolio story

```text
Autonomy / SLAM
      ↓
Safety-governed embodiment
      ↓
Manipulation / kinematics
      ↓
Embedded electronics / PCB
      ↓
Low-level systems engineering
      ↓
Cognitive runtime architecture
```

The goal is not to collect disconnected demos. Each flagship project demonstrates a different engineering layer while following the same evidence discipline.

---

## Supporting robotics projects

- **[line-following-robot](https://github.com/VivekVRobo/line-following-robot)** — control stack, PID behavior, corrected sensor-bar simulation geometry, regression testing, and robustness sweeps.
- **[cv-object-sorter](https://github.com/VivekVRobo/cv-object-sorter)** — OpenCV perception → decision → actuation pipeline, passage-safe triggering, synthetic threshold-contract evidence, and labeled-image evaluation tooling.
- **[gesture-controlled-robot](https://github.com/VivekVRobo/gesture-controlled-robot)** — MediaPipe gesture control with rotation-aware landmark geometry, temporal command stabilization, immediate STOP fail-safe, serial heartbeat, and MCU watchdog behavior.

---

## Engineering stack

| Area | Technologies |
| --- | --- |
| **Robotics** | ROS 2, SLAM, Gazebo, TF, localization, kinematics, trajectory evaluation |
| **Computer vision** | OpenCV, MediaPipe, HSV/contour pipelines, offline evaluation |
| **Embedded systems** | Arduino, servo control, PCA9685, serial protocols, watchdogs |
| **Electronics** | KiCad, PCB design workflow, motor drivers, electrical/current/thermal modeling |
| **Systems** | C++20, raw sockets, HTTP/1.1, Linux `epoll`, concurrency, benchmarking |
| **Software** | Python, FastAPI, Flask, SQLite, React, TypeScript, automated testing |
| **Engineering workflow** | Git, GitHub Actions, CI, machine-readable evidence, reproducible runbooks |

---

## Engineering principles

### Measure before claiming

Simulation results stay simulation results. Analytical results stay analytical results. Physical claims require physical evidence.

### Reproducibility over screenshots

Important experiments should preserve the **exact commit, environment, configuration, raw artifacts, metrics, and failure cases** so another developer can reproduce or challenge the result.

### Deterministic safety around actuation

AI, perception, UI, and character layers should not directly command physical actuators. Motion authority belongs behind explicit planning, validation, safety supervision, and hardware boundaries.

### Build systems that can be inspected

Architecture, failure modes, limitations, evidence maturity, and release gates are treated as part of the engineering—not as afterthoughts.

---

## Current evidence milestones

- **SLAM:** execute and publish the first genuine Gazebo benchmark evidence bundle.
- **vhttp:** run the M6B.2 thread-pool vs `epoll` campaign on a documented Linux/WSL2 host.
- **3-DOF arm:** add real endpoint-accuracy and repeatability measurements when physical hardware is available.
- **Motor-driver PCB:** progress from analytical/CAD validation to fabrication and bench evidence.
- **RCI:** replace engineering-predicted embodiment values with measured HIL/physical evidence when hardware exists.
- **Aurelia:** keep deterministic runtime evidence strong while avoiding unsupported AGI, production-scale, or physical-autonomy claims.

---

## What I optimize for

**Robotics systems that are measurable, reproducible, safety-conscious, and honest about what has actually been demonstrated.**
