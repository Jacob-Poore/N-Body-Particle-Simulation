import math # Used because it's faster than calculating it with my own functions
import matplotlib.pyplot as plt 
from matplotlib import rcParams # For Fonts and Removing Toolbar
from matplotlib.animation import FuncAnimation # To animate the plot
from matplotlib.widgets import Button, Slider, TextBox # User GUI

rcParams['font.family'] = 'DejaVu Sans Mono' 
rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Helvetica', 'Verdana']
plt.rcParams['toolbar'] = 'None'

# Parameters
dt = 0.005  # Smaller time step for stability
v = 1.0     # Initial speed
L = 1.0     # Initial distance

# Initialize particles 
def create_particles(): # Initial conditions 
    particles = [
        {'x': -L/3, 'y': .3, 'radius': 0.1, 'mass': 2, 'color': 'xkcd:red pink', 'vx': v/2, 'vy': .1, 'trajectory': []},
        {'x': L/3, 'y': -.3, 'radius': 0.1, 'mass': 2, 'color': 'xkcd:bright turquoise', 'vx': -v/2, 'vy': -.1, 'trajectory': []}]
    return particles

particles = create_particles()

# Gravity force between two particles
def gravity(p1, p2):
    G = 1.0  # Gravitational constant (required)
    dx = p2['x'] - p1['x']
    dy = p2['y'] - p1['y'] 
    distance_squared = dx**2 + dy**2 # Turning two vectors into a scalar
    distance = math.sqrt(distance_squared) 
    force = G * p1['mass'] * p2['mass'] / distance**2 
    fx = force * (dx / distance) # Force of Gravity between two bodies formula (x,y)
    fy = force * (dy / distance)
    return fx, fy, distance 

# Update position and record trajectory
def update_position(i, dt):
    particles[i]['x'] += particles[i]['vx'] * dt # Distance is vecolcity * time
    particles[i]['y'] += particles[i]['vy'] * dt
    
# Update velocity based on force
def update_velocity(i, force, dt):
        fx, fy = force
        ax = fx / particles[i]['mass'] # Equation from Newton's Law F=MA
        ay = fy / particles[i]['mass']
        particles[i]['vx'] += ax * dt # Change in velocity is acceleration times changes in time
        particles[i]['vy'] += ay * dt

# Main integration step
def integrate(dt):
    for i in range(len(particles)):
        net_force = [0, 0] # Resets netforce for each particle
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
            particles[i]['trajectory'].pop(0)"""  # Add this if performance is struggling for long time

# Plotting function for MatplotLib (Plot calls integreate, which determines where to plot)
def plot(frame):
    if is_playing:
        integrate(dt)
    ax.cla()
    ax.set_aspect('equal', 'box')
    ax.set_title('Two-Body Simulation', color='white')
    for p in particles:
        if p['trajectory']:
            x_vals, y_vals = zip(*p['trajectory'])
            ax.plot(x_vals, y_vals, color=p['color'], linewidth=0.75, alpha=0.7) # Plot the trajectories
        ax.scatter(p['x'], p['y'], color='white', s=100, alpha=0.4, edgecolors='none') # Plot the particles with an outer ring, making them look "emissive"
        ax.scatter(p['x'], p['y'], color=p['color'], s=70, alpha=0.7, edgecolors='none') # Plot the particles

# Create Plot
fig, ax = plt.subplots(figsize=(16, 9))
try:
    fig.canvas.manager.window.geometry("+0+0")
except:
    pass
# Making Plot look cooler
fig.canvas.manager.set_window_title('Two-Body Gravitational Simulation')
fig.patch.set_facecolor('xkcd:almost black')
ax.set_frame_on(False)
ax.tick_params(axis='both', colors='white')


# Button Controls
is_playing = False # Creating a toggle for the eventse

def toggle(event): 
    global is_playing # toggles global assignment
    is_playing = not is_playing
    play_button.label.set_text('Pause' if is_playing else 'Play') # Changes text depending on toggle
    play_button.color = 'grey' if is_playing else 'xkcd:scarlet' # Changes color depending on toggle
 
def reset(event): # Recreates my particles from the beginning, reseting them without needing to mess with matplotlib
    global particles
    particles = create_particles() 

# Play/Pause button
ax_play = plt.axes([0.83, 0.90, 0.15, 0.06]) # Creates button body
play_button = Button(ax_play, 'Play', color='xkcd:scarlet', hovercolor='0.8')
play_button.label.set_color('white'), play_button.label.set_fontweight('light')
play_button.on_clicked(toggle) # Calls toggle on click

# Reset button
ax_reset = plt.axes([0.83, 0.82, 0.15, 0.06]) # Creates button body
reset_button = Button(ax_reset, 'Reset', color='0.7', hovercolor='0.8')
reset_button.label.set_color('white')
reset_button.on_clicked(reset) # Calls reset on click


# Animation
ani = FuncAnimation(fig, plot, cache_frame_data=False, interval=15) # Function call 
plt.show() 
