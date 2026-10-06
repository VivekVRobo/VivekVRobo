<div align="center">

# Vivek Vala

### Robotics & Autonomous Systems · Embedded Systems · Systems Engineering

I build **physical robots, autonomy software, embedded control systems, and low-level software** with an emphasis on measurable results, reproducibility, and explicit evidence.

[**Portfolio**](https://vivek-vala-portfolio.vercel.app/) · [**Physical robotic arm**](https://github.com/VivekVRobo/gesture-controlled-robotic-arm) · [**ROS 2 / SLAM**](https://github.com/VivekVRobo/slam-robot-ros2)

</div>

---

## Recruiter quick scan

| Area | Evidence |
| --- | --- |
| **Physical robotics** | Wearable MPU6050 + nRF24L01 gesture control driving a real multi-joint robotic arm; physical actuation video and bench evidence published |
| **ROS 2 / autonomy** | Reproducibility-first SLAM stack with Gazebo ground truth, ATE/RPE tooling, loop-closure evaluation and rosbag regression; runtime benchmark evidence is still gated |
| **Embedded / controls** | Arduino, PCA9685, servo control, watchdogs, kinematics, calibration tooling, motor-control and PCB work |
| **Systems programming** | C++20 HTTP/1.1 server from raw sockets with secure static files, bounded concurrency and Linux `epoll` runtime |
| **Open source** | [FusionCore PR #96](https://github.com/manankharwar/fusioncore/pull/96) merged upstream: fixed GNSS TF/frame validation and added focused tests |

---

## Start here

<table>
<tr>
<td width="33%" valign="top">

### 🤖 Gesture-Controlled Robotic Arm
**Best physical-hardware proof**

Wearable MPU6050 gesture control over nRF24L01 driving a multi-joint robotic arm with real actuation evidence.

**Stack:** Arduino · C++ · MPU6050 · nRF24L01 · PCA9685

[Repository →](https://github.com/VivekVRobo/gesture-controlled-robotic-arm)

</td>
<td width="33%" valign="top">

### 🗺️ ROS 2 SLAM Benchmarking
**Autonomy & localization**

2D LiDAR SLAM stack designed around simulator ground truth, trajectory metrics, loop-closure measurement and reproducible evidence.

**Stack:** ROS 2 · Gazebo · LiDAR · Python · SLAM Toolbox

[Repository →](https://github.com/VivekVRobo/slam-robot-ros2)

</td>
<td width="33%" valign="top">

### 🌐 HTTP Server From Scratch
**Systems engineering**

C++20 HTTP/1.1 server built from raw sockets with parser, routing, secure static files, bounded thread-pool concurrency and Linux `epoll`.

**Stack:** C++20 · sockets · HTTP/1.1 · epoll · CMake · CI

[Repository →](https://github.com/VivekVRobo/http-server-from-scratch)

</td>
</tr>
</table>

---

## Selected engineering work

| Project | Engineering focus | Current evidence |
| --- | --- | --- |
| **[gesture-controlled-robotic-arm](https://github.com/VivekVRobo/gesture-controlled-robotic-arm)** | Wireless wearable control, sensor fusion, RF telemetry, servo actuation | **Physical hardware demo + bench evidence published** |
| **[slam-robot-ros2](https://github.com/VivekVRobo/slam-robot-ros2)** | ROS 2 SLAM, Gazebo ground truth, ATE/RPE, loop closure, rosbag regression | Static contracts + ROS build CI verified; runtime benchmark still pending |
| **[3dof-robotic-arm](https://github.com/VivekVRobo/3dof-robotic-arm)** | Analytic FK/IK, Cartesian planning, servo mapping, validation tooling | Numerical/software validation complete; physical endpoint accuracy pending |
| **[custom-pcb-motor-driver](https://github.com/VivekVRobo/custom-pcb-motor-driver)** | DRV8848 motor-driver design, current/thermal modeling, KiCad workflow | Engineering/CAD evidence available; fabrication and bench validation pending |
| **[http-server-from-scratch](https://github.com/VivekVRobo/http-server-from-scratch)** | Raw sockets, HTTP parsing, secure static files, bounded concurrency, `epoll` | Linux + Windows CI verified; controlled performance results pending |
| **[universal-brain](https://github.com/VivekVRobo/universal-brain)** | Local-first executive runtime, permissions, durable missions, recovery, verification | Engineering checkpoints verified; real-environment endurance evidence in progress |

---

## Open-source contribution

### FusionCore — merged upstream

[**PR #96: fix GNSS TF validation using the configured or message frame**](https://github.com/manankharwar/fusioncore/pull/96)

- fixed false GNSS TF warnings caused by assuming a hard-coded `gnss_link` frame;
- added configurable/message-derived GNSS frame resolution;
- updated lever-arm lookup behavior;
- added focused unit coverage;
- merged into the upstream repository.

This is the strongest external validation on the profile today because the work was reviewed and accepted outside my own repositories.

---

## Supporting robotics projects

- **[line-following-robot](https://github.com/VivekVRobo/line-following-robot)** — control stack, PID behavior, deterministic simulation, telemetry and robustness sweeps.
- **[cv-object-sorter](https://github.com/VivekVRobo/cv-object-sorter)** — OpenCV perception → decision → actuation pipeline with deterministic software evaluation tooling.
- **[gesture-controlled-robot](https://github.com/VivekVRobo/gesture-controlled-robot)** — MediaPipe-based mobile-robot command stack with temporal stabilization, immediate STOP behavior and watchdog protection.

---

## Engineering stack

**Robotics:** ROS 2 · SLAM · Gazebo · TF · localization · kinematics · trajectory evaluation  
**Embedded:** Arduino · C/C++ · PCA9685 · serial protocols · watchdogs · servo/motor control  
**Vision:** OpenCV · MediaPipe · HSV/contour pipelines · evaluation tooling  
**Electronics:** KiCad · motor drivers · current/thermal modeling · PCB workflow  
**Systems:** C++20 · raw sockets · HTTP/1.1 · Linux `epoll` · concurrency · benchmarking  
**Software:** Python · FastAPI · Flask · SQLite · React · TypeScript · automated testing  
**Workflow:** Git · GitHub Actions · CI · reproducible runbooks · machine-readable evidence

---

## Evidence policy

I try to keep claims at the same level as the evidence:

- **simulation stays simulation;**
- **software validation is not hardware validation;**
- **physical claims require physical measurements or direct hardware evidence;**
- important experiments should preserve the commit, environment, configuration, raw artifacts, metrics and failure cases.

---

## Current proof priorities

1. publish a genuine end-to-end Gazebo SLAM benchmark bundle;
2. measure real endpoint accuracy and repeatability on the 3-DOF arm;
3. fabricate and bench-test the motor-driver PCB;
4. publish controlled performance results for the C++ HTTP server;
5. continue contributing scoped fixes to external robotics/software projects.

---

## Contact / collaboration

I am interested in **robotics, autonomous systems, ROS 2, embedded systems, computer vision, controls, and systems engineering** work where implementation can be backed by reproducible evidence.

[**Portfolio**](https://vivek-vala-portfolio.vercel.app/) · [**GitHub**](https://github.com/VivekVRobo)
