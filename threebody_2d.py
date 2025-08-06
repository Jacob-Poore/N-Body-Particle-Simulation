import math
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, Slider, TextBox

rcParams['font.family'] = 'Cambria'
rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Helvetica', 'Verdana']
plt.rcParams['toolbar'] = 'None'

# Parameters
dt = 0.005  # Smaller time step for stability
v = 1.0     # Initial speed
L = 1.0     # Initial distance
soft = 0.01 # Softening Force 

# Initialize particles in an equilateral triangle
def create_particles():
    particles = [
        {'x': -L/2, 'y': 0, 'radius': 0.1, 'mass': 2, 'color': 'xkcd:red pink', 'vx': v, 'vy': 0, 'trajectory': []},
        {'x': L/2, 'y': 0, 'radius': 0.1, 'mass': 2, 'color': 'xkcd:bright magenta', 'vx': -v/2, 'vy': v * 0.8660254037844386, 'trajectory': []},
        {'x': 0, 'y': L * 0.8660254037844386, 'radius': 0.1, 'mass': 1, 'color': 'xkcd:bright turquoise', 'vx': -v/2, 'vy': -v * 0.8660254037844386, 'trajectory': []}]
    return particles

particles = create_particles()

# Gravity force between two particles
def gravity(p1, p2):
    G = 1.0 
    dx = p2['x'] - p1['x']
    dy = p2['y'] - p1['y']
    distance_squared = dx**2 + dy**2 # Turning two vectors into a scalar
    distance = math.sqrt(distance_squared)
    force = G * p1['mass'] * p2['mass'] / distance**2
    fx = force * (dx / distance)
    fy = force * (dy / distance)
    return fx, fy, distance

# Update position and record trajectory
def update_position(i, dt):
    particles[i]['x'] += particles[i]['vx'] * dt  # Distance is vecolcity * time
    particles[i]['y'] += particles[i]['vy'] * dt
    
# Update velocity based on force
def update_velocity(i, force, dt):
        fx, fy = force
        ax = fx / particles[i]['mass'] # Equation from Newton's Law F=MA
        ay = fy / particles[i]['mass']
        particles[i]['vx'] += ax * dt # Change in velocity is acceleration times change in time
        particles[i]['vy'] += ay * dt

# Main integration step
def integrate(dt):
    for i in range(len(particles)):
        net_force = [0, 0]
        for j in range(len(particles)):
            if i != j: # Makes sure only the other particles effect its own net force (if i = 1 and j = 1 gravity isn't called)
                fx, fy, distance = gravity(particles[i], particles[j])
                net_force[0] += fx
                net_force[1] += fy
        update_velocity(i, net_force, dt) # Updates velocity for each particle first
    for i in range(len(particles)): # Updates Position, Stores Trajectories
        update_position(i, dt)
        particles[i]['trajectory'].append((particles[i]['x'], particles[i]['y']))
        """if len(particles[i]['trajectory']) > 1000:
            particles[i]['trajectory'].pop(0)""" # Add this if performance is struggling for long time

# Plotting function for MatplotLib (Plot calls integreate, which determines where to plot)
def plot(frame):
    if is_playing:
        integrate(dt)
    ax.cla()
    ax.set_title('Three-Body Simulation', color='white')
    for p in particles:
        if p['trajectory']:
            x_vals, y_vals = zip(*p['trajectory'])
            ax.plot(x_vals, y_vals, color=p['color'], linewidth=0.75, alpha=0.7) # Plot the trajectories
        ax.scatter(p['x'], p['y'], color='white', s=100, alpha=0.4, edgecolors='none') # Plot the particles, making them look "emissive"
        ax.scatter(p['x'], p['y'], color=p['color'], s=70, alpha=0.7, edgecolors='none') # Plot the particles

# Create Plot
fig, ax = plt.subplots(figsize=(16, 9))
try:
    fig.canvas.manager.window.geometry("+0+0")
except:
    pass
fig.canvas.manager.set_window_title('Three-Body Gravitational Simulation')
fig.patch.set_facecolor('xkcd:almost black')
ax.set_frame_on(False)
ax.tick_params(axis='both', colors='white')


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
