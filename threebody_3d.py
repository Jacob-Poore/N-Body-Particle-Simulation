import math
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, Slider, TextBox
from mpl_toolkits.mplot3d import Axes3D

rcParams['font.family'] = 'Cambria'
rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Helvetica', 'Verdana']
plt.rcParams['toolbar'] = 'None'

# Parameters
dt = 0.005  # Smaller time step for stability
v = 1.0     # Initial speed
L = 1.0     # Initial distance
soft = 0.05 # Softening Force

# Initialize particles in an equilateral triangle in 3D
def create_particles():
    particles = [
        {'x': -L/2, 'y': 0, 'z': 0, 'radius': 0.1, 'mass': 10, 'color': 'xkcd:red pink', 'vx': 0, 'vy': v, 'vz': 0, 'trajectory': []},
        {'x': L/2, 'y': 0, 'z': 0, 'radius': 0.1, 'mass': 1, 'color': 'xkcd:bright magenta', 'vx': 0, 'vy': -v, 'vz': 0, 'trajectory': []},
        {'x': 0, 'y': L * 0.8660254037844386, 'z': L / 1.7320508075688772 , 'radius': 0.1, 'mass': .1, 'color': 'xkcd:bright turquoise', 'vx': v/2, 'vy': 0, 'vz': v/2, 'trajectory': []}
    ]
    return particles

particles = create_particles()

# Gravity force between two particles (3D)
def gravity(p1, p2):
    G = 1.0  # Gravitational constant
    dx = p2['x'] - p1['x']
    dy = p2['y'] - p1['y']
    dz = p2['z'] - p1['z']
    distance_squared = dx**2 + dy**2 + dz**2
    distance = math.sqrt(distance_squared)
    force = G * p1['mass'] * p2['mass'] / distance_squared
    fx = force * (dx / distance)
    fy = force * (dy / distance)
    fz = force * (dz / distance)
    return fx, fy, fz, distance

# Update position and record trajectory in 3D
def update_position(i, dt):
    particles[i]['x'] += particles[i]['vx'] * dt
    particles[i]['y'] += particles[i]['vy'] * dt
    particles[i]['z'] += particles[i]['vz'] * dt
    
# Update velocity based on force in 3D
def update_velocity(i, force, dt):
    fx, fy, fz = force
    ax = fx / particles[i]['mass']
    ay = fy / particles[i]['mass']
    az = fz / particles[i]['mass']
    particles[i]['vx'] += ax * dt
    particles[i]['vy'] += ay * dt
    particles[i]['vz'] += az * dt

# Main integration step
def integrate(dt):
    for i in range(len(particles)):
        net_force = [0, 0, 0]
        for j in range(len(particles)):
            if i != j:
                fx, fy, fz, distance = gravity(particles[i], particles[j])
                net_force[0] += fx
                net_force[1] += fy
                net_force[2] += fz
        update_velocity(i, net_force, dt) # Updates velocity for each particle first
    for i in range(len(particles)): # Updates Position, Stores Trajectories
        update_position(i, dt)
        particles[i]['trajectory'].append((particles[i]['x'], particles[i]['y'], particles[i]['z']))

# Plotting function for MatplotLib (Plot calls integrate, which determines where to plot)
def plot(frame):
    if is_playing:
        integrate(dt)
    ax.cla()
    ax.set_title('Three-Body Simulation', color='white')
    for p in particles:
        if p['trajectory']:
            x_vals, y_vals, z_vals = zip(*p['trajectory'])
            ax.plot(x_vals, y_vals, z_vals, color=p['color'], linewidth=0.75, alpha=0.7)  # Plot the trajectories
        ax.scatter(p['x'], p['y'], p['z'], color='white', s=100, alpha=0.4, edgecolors='none') # Plot the particles
        ax.scatter(p['x'], p['y'], p['z'], color=p['color'], s=70, alpha=0.7, edgecolors='none') # Plot the particles

# Create Plot
fig = plt.figure(figsize=(16, 9))
ax = fig.add_subplot(111, projection='3d')  # Use 3D projection
try:
    fig.canvas.manager.window.geometry("+0+0")
except:
    pass
fig.canvas.manager.set_window_title('Three-Body Gravitational Simulation')
fig.patch.set_facecolor('xkcd:almost black')
ax.set_facecolor('black')
ax.tick_params(axis='both', colors='white')
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Now set color to white (or whatever is "invisible")
ax.xaxis.pane.set_edgecolor('red')
ax.yaxis.pane.set_edgecolor('cyan')
ax.zaxis.pane.set_edgecolor('magenta')

# Button Controls
is_playing = False

def toggle(event):
    global is_playing
    is_playing = not is_playing
    play_button.label.set_text('Pause' if is_playing else 'Play')
    play_button.color = 'grey' if is_playing else 'xkcd:scarlet'

def reset(event):
    global particles
    particles = create_particles() 

# Play/Pause button
ax_play = plt.axes([0.83, 0.90, 0.15, 0.06])
play_button = Button(ax_play, 'Play', color='xkcd:scarlet', hovercolor='0.8')
play_button.label.set_color('white'), play_button.label.set_fontweight('light')
play_button.on_clicked(toggle)

# Reset button
ax_reset = plt.axes([0.83, 0.82, 0.15, 0.06])
reset_button = Button(ax_reset, 'Reset', color='0.7', hovercolor='0.8')
reset_button.label.set_color('white')
reset_button.on_clicked(reset)

# Animation
ani = FuncAnimation(fig, plot, frames=range(60), interval=1)
plt.show()
