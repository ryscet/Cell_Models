# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:11:54 2015

@author: ryszardcetnarski
"""

import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import animation
## setup parameters and state variables
T       = 50                  # total time to simulate (msec)
dt      = 0.125               # simulation time step (msec)
time    = np.arange(0, T+dt, dt) # time array
t_rest  = 0                   # initial refractory time

## LIF properties
Vm      = np.zeros(len(time)) 
#Vm[0] = 1.5   # potential (V) trace over time 
Rm      = 1                   # resistance (kOhm)
Cm      = 10                  # capacitance (uF)
tau_m   = Rm*Cm               # time constant (msec)
tau_ref = 4                   # refractory period (msec)
Vth     = 1                   # spike threshold (V)
V_spike = 0.5                 # spike delta (V)

## Input stimulus
I       =  1.5                # input current (A)

## iterate over each time step
##This adds the input I multiplied by resistance Rm and divided by time
#If the transformed input exceeds threshold Vth spike is generated (0.5 is added to the Vm) 
for i, t in enumerate(time): 
  if t > t_rest: 
    Vm[i] = Vm[i-1] + (-Vm[i-1] + I*Rm) / tau_m * dt
    if Vm[i] >= Vth:
      Vm[i] += V_spike
      t_rest = t + tau_ref


#------------This part is just for plotting-----------------

#This is the original plot from the code in the web
## plot membrane potential trace  
plot(time, Vm)
title('Leaky Integrate-and-Fire Example')
ylabel('Membrane Potential (V)')
xlabel('Time (msec)')
ylim([0,2])

show()

#This is are the real time plots I added
#This plot should show the activity of neurons in the network (simplified to a 2d grid)
fig = plt.figure()
space_ax = fig.add_subplot(111)
grid = np.zeros(4).reshape(2,2)
bp = space_ax.imshow(grid, interpolation = 'none')

#This plot should show the time course of the activity. None of it is in real time really though. It is a replay of the simulation
def simData():
    t_max = 10.0
    dt = 0.05
    x = 0.0
    t = 0.0
    i = 0
    while t < t_max:
        #Here the y is taken from the history of activity (Vm)
        y = Vm[i]
        t = t + dt
        i = i +1
        yield y, t

 
def simPoints(simData):
    y, t = simData[0], simData[1]
    time_text.set_text(time_template%(t))
    line.set_data(t, y)
    return line, time_text
 

fig = plt.figure()
ax = fig.add_subplot(111)

line, = ax.plot([], [], 'bo', ms=10)
ax.set_ylim(0, 1.5)
ax.set_xlim(0, 10)
##
time_template = 'Time = %.1f s'    # prints running simulation time
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

ani = animation.FuncAnimation(fig, simPoints, simData, blit=False, interval=10, repeat=True)
anim_space = animation.FuncAnimation(fig,  space_animate, frames=30, interval=20, blit=True)


plt.show()
