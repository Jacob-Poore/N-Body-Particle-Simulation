N-Body Particle Simulation
A real-time simulation of gravitational interactions between particles in 2D and 3D space, implemented in Python with Matplotlib.

Features
2D and 3D simulations of gravitational particle systems
Newtonian gravity physics with softening term to prevent singularities
Forward Euler integration method for numerical computation
Real-time animation with trajectory visualization
Interactive controls for simulation management
Three-body problem demonstration scenarios
Entirely within Python

Requirements
Python 3.6 or higher
Matplotlib
Numpy

Usage
Run Menu.py to open the GUI menu, or go straight to the individual simulations. 

Physics Implementation
The simulation implements classical Newtonian gravity with the following computational steps performed each frame:
Force Calculation
Gravitational forces between all particle pairs are computed using:
F = G * (m1 * m2) / (r^2 + ε^2)

Particle velocities are updated using the forward Euler method:
v_new = v_old + a * Δt

Particle positions are updated using:
x_new = x_old + v * Δt

Visualization Update
The display is refreshed to show current particle positions and trajectory trails.

Configuration Parameters
Key simulation parameters can be adjusted in the source code:
t: step size for numerical integration
v: Initial velocity magnitude for particles
L: Initial spacing between particles
soft: Gravity softening factor (learn more about this here https://academic.oup.com/mnras/article/314/3/475/969154).
From just these parameters, it is possible to model a variety of periodic and aperiodic solutions of the three body problem. 

Customization
Modify the create_particles() function to customize:
Particle masses
Initial positions
Initial velocities
Visual appearance (colors)

License
MIT License
Additional Information
For a more in-depth project description and additional physics simulations, visit: jacobpoore.wescreates.wesleyan.edu/projects
