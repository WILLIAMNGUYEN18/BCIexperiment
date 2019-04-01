import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import serial

# Compute the x and y coordinates for points on a sine curve 
ser = serial.Serial('COM5')

#arange function returns evenly spaced numeric values within an interval, stored as a NumPy array (i.e., an ndarray object).
#
#Using this for x axis of plot
xAxis = np.arange(0, 5)

# First set up the figure, the axis, and the plot element we want to animate
#fig = plt.figure()
#ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
#line, = ax.plot([], [], lw=2)
#ylim should be from 0 to 1024


# First set up the figure, the axis, and the plot element we want to animate
#https://www.geeksforgeeks.org/graph-plotting-python-set-2/
#old fig and ax
#fig, ax = plt.subplots()

fig = plt.figure()
ax = plt.axes(xlim = (0,100), ylim = ())

#zeros function returns a new array of given shape and type, with zeros.
#shape, dtype = None, order = ‘C’
y = np.zeros((5), dtype=int)
line, = ax.plot(xAxis, y)


#filling y values corresponding to x values before we start.
for x in xAxis:    
    y[x] = ser.readline() # fills y axis w data before going to dynamic graph
    print(y[x])





#Positional Read:
#Note that the index -1 represents the last element. 
# That's because negative indices in Python (and NumPy) 
# are counted from the end, so -1 is the last, -2 is the 
# one before last and -len is actually the first element

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

#bring up the plot after creating it (animating)
plt.show()
                    