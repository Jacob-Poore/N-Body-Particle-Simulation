# N-Body Particle Simulation

A real-time simulation of gravitational interactions between particles in 2D and 3D space, implemented in Python using Matplotlib.

---

## Features

- Simulates gravitational interactions in 2D and 3D
- Newtonian gravity with softening to prevent singularities
- Forward Euler integration for numerical updates
- Real-time animation with trajectory visualization
- Interactive controls for play, pause, and reset
- Demonstrates various three-body problem scenarios
- Built entirely with native Python libraries

---

## Requirements

- Python 3.6+
- `matplotlib`
- `numpy`

Install dependencies via pip:

```bash
pip install matplotlib numpy
```

---

## Usage

Run the main menu:

```bash
python Menu.py
```

Alternatively, you can run individual simulation scripts directly.

---

## Physics Implementation

Classical Newtonian gravity is used, with computations updated in real-time per frame:

### Force Calculation
For each particle pair:

```
F = G * (m1 * m2) / (r² + ε²)
```

Where:
- `G` is the gravitational constant
- `ε` is the softening factor to avoid singularities

### Velocity Update (Forward Euler)

```
v_new = v_old + a * Δt
```

### Position Update

```
x_new = x_old + v * Δt
```

### Visualization

Particle positions and trajectory trails are redrawn each frame to reflect current system state.

---

## Configuration Parameters

You can modify the following simulation settings in the source code:

| Parameter | Description                         |
|-----------|-------------------------------------|
| `t`       | Time step size                      |
| `v`       | Initial velocity magnitude          |
| `L`       | Initial spacing between particles   |
| `soft`    | Gravity softening factor ([reference](https://academic.oup.com/mnras/article/314/3/475/969154)) |

These parameters allow you to model both periodic and chaotic solutions of the three-body problem.

---

## Customization

To modify the particle system, edit the `create_particles()` function:

- Adjust mass, position, and velocity per particle
- Change particle appearance (color, size)

---

## Additional Information

For an extended project overview and more physics-based simulations, visit:

**[jacobpoore.wescreates.wesleyan.edu/projects](https://jacobpoore.wescreates.wesleyan.edu/projects)**
