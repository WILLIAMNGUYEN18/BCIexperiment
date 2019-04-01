import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial

# Compute the x and y coordinates for points on a sine curve 
ser = serial.Serial('COM5')


# First set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots()


#fig = plt.figure()
#ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
#line, = ax.plot([], [], lw=2)

xAxis = np.arange(0, 5)
y = np.zeros((5), dtype=int)
line, = ax.plot(xAxis, y)

#reading first bit in serial
ser.read() #Effectively sending it to garbage to not get a chopped up serial byte
for x in xAxis:    
    y[x] = ser.readline() # fills y axis w data before going to dynamic graph
    print(y[x])


# initialization function: plot the background of each frame
def init():  # first frame
    global line
    line.set_data(xAxis, y)
    return line,

# animation function.  This is called sequentially
def animate(i):
    global y
    global line
    #y = np.delete(y, 0)
    y = np.append(y, [ser.read()])
    line.set_ydata(y)  # update the data.
    return line,

plt.title("ADC data") 

# Plot the points using matplotlib 
# call the animator.  blit=True means only re-draw the parts that have changed.
ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=2, blit=True, save_count=50)
plt.show()










