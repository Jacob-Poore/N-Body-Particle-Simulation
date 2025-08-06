import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.widgets import Button

# Setting up fonts in matplotlib
rcParams['font.family'] = 'DejaVu Sans Mono'
rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Helvetica', 'Verdana']
plt.rcParams['toolbar'] = 'None'

def program1(event):
    #plt.close(fig)
    try:
        import twobody
    except:
        print('Failed to open twobody')
        
    
def program2(event):
    #plt.close(fig)
    import threebody_2d

def program3(event):
    #plt.close(fig)
    try:
        import threebody_3d
    except:
        print('Failed to open threebody')


# Create the figure and axis
fig, ax = plt.subplots(figsize=(16, 9))
try:
    fig.canvas.manager.window.geometry("+0+0")
except:
    pass

fig.patch.set_facecolor('xkcd:almost black')
fig.canvas.manager.set_window_title("Gravitational Simulator Menu")
ax.set_xticks([]), ax.set_yticks([]), ax.set_frame_on(False)
ax.text(0.5, 0.8, "Choose a Simulation", fontsize=16, ha='center', transform=fig.transFigure, color='white')

# Create buttons
ax_button1 = plt.axes([0.35, 0.6, 0.3, 0.1])
ax_button2 = plt.axes([0.35, 0.45, 0.3, 0.1])
ax_button3 = plt.axes([.35, 0.3, 0.3, 0.1])

button_body1= Button(ax_button1, "2-Body", color = 'xkcd:light sky blue')
button_body2= Button(ax_button2, "3-Body", color = 'xkcd:sky blue')
button_body3= Button(ax_button3, "3-Body (3D!)", color = 'xkcd:french blue')

button_body1.on_clicked(program1)
button_body2.on_clicked(program2)
button_body3.on_clicked(program3)
plt.show()
