# Potentially use redraw instead of animate in matplot lib

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial

# Compute the x and y coordinates for points on a sine curve 
ser = serial.Serial('COM7')
fig, ax = plt.subplots()


xAxis = np.arange(0, 100)
y = np.zeros((100), dtype=int)
line, = ax.plot(xAxis, y)
ser.readline() #so i dont get a chopped up serial byte
for x in xAxis:    
    y[x] = ser.readline() # fills y axis w data before going to dynamic graph
    print(y[x])

def displayY():
     print(y)

def init():  # first frame
    global line
    line.set_data(xAxis, y)
    return line,

def animate(i):
    global y
    global line
    #print("before delete")
    #displayY()
    y = np.roll(y, 1)
    #print("after delete")
   # displayY()
    y[99] = ser.readline()
    #print("after append")
    #displayY()
    line.set_ydata(y)  # update the data.
    return line,

plt.ylim(0, 1024)
plt.title("ADC data") 

# Plot the points using matplotlib 
ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=2, blit=True, save_count=50)
plt.show()










