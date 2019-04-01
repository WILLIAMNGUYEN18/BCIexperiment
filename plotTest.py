# Potentially use redraw instead of animate in matplot lib

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
import collections

# Compute the x and y coordinates for points on a sine curve 
ser = serial.Serial('COM6')
fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(0, 1024))

y = collections.deque()


xAxis = np.arange(0, 100)
#y = np.zeros((100), dtype=int)

ser.readline() #so i dont get a chopped up serial byte
for x in xAxis:    
    y.appendleft(int(ser.readline().rstrip())) # fills y axis w data before going to dynamic graph
    #print(y[x])
line, = ax.plot(xAxis, y)

def init():  # first frame
    global line
    line.set_data(xAxis, y)
    return line,

def animate(i):
    global y
    global line
    #print("before delete")
    #displayY()
    y.pop()
    #print(y)
   # displayY()
    y.appendleft(int(ser.readline().rstrip()))
    #print(y)
    #displayY()
    line.set_ydata(y)  # update the data.
    return line,


plt.title("ADC data") 
#ax.set_ylim(0, 1024, emit=True, auto=True)
plt.yticks(np.arange(0, 1024, step=100), np.arange(0, 1024, step=100))

# Plot the points using matplotlib 
ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=2, blit=True, save_count=50)
plt.show()










