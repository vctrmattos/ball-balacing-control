#Ball balacing with PID control

This project aims to create a control system to keep a ball balanced on a tiltable surface. Using a webcam to detect the ball's position and two servo motors located perpendicularly, we implemented a PID control to adjust the surface tilt and keep the ball in the desired position. As of now, the project is a work in progress.

## Completed:
### Webcam
- [x] Code for the surface position: Implements a computer vision algorithm to detect the surface position.
- [x] Code for the ball position: Implements a computer vision algorithm to detect the ball's position on the surface.

### Arduino
- [x] Data transmission from Python to Arduino via serial connection

## In Progress:
- [ ] Finish building the project: Currently assembling the physical components and testing mechanical stability;
- [ ] Implementation of PID control with two servo motors: Developing the code to control the servo motors based on the PID algorithm;
- [ ] Optimization of PID control parameters;
- [ ] Refinements in position detection;
- [ ] Robustness and performance testing: Conducting tests to ensure the system operates reliably in various conditions.
- [ ] Implementation of additional features: Adding extra functionalities such as a user interface for manual control.


