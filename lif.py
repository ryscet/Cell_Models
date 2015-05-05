# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:11:54 2015

@author: ryszardcetnarski
"""

import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import animation

class IntegrateFire:
    'Generates spikes using a simple neuron model with current input'
#TODO T is a simulation time, should be global/static    

    T = 1000                  # total time to simulate (msec) // 1sec = 1000 msec so we are doing 1 sec simulations

    def __init__(self, _input):
        ## Simulation parameters

        self.dt = 1                                     # simulation time step (msec)
        self.time = np.arange(0, self.T + self.dt, self.dt) # time array
        self.t_rest = 0                                     # initial refractory time
        
        ## LIF properties
        self.Vm = np.zeros(len(self.time))      # potential (V) trace over time 
        self.Rm      = 1                   # resistance (kOhm)
        self.Cm      = 10                  # capacitance (uF)
        self.tau_m   = self.Rm*self.Cm     # time constant (msec)
        self.tau_ref = 4                   # refractory period (msec)
        self.Vth     = 1                   # spike threshold (V)
        self.V_spike = 0.5                 # spike delta (V)

        ## Input stimulus
        self.I  =  _input                # input current (A)

## iterate over each time step
##This adds the input I multiplied by resistance Rm and divided by time
#If the transformed input exceeds threshold Vth spike is generated (0.5 is added to the Vm) 
    def Simulate(self):        
        ## iterate over each time step
        for i, t in enumerate(self.time): 
            if t > self.t_rest:
                self.Vm[i] = self.Vm[i-1] + (-self.Vm[i-1] + self.I*self.Rm) / self.tau_m * self.dt
                if self.Vm[i] >= self.Vth:
                    self.Vm[i] += self.V_spike
                    self.t_rest = t + self.tau_ref
        return self.Vm

#------------This part is just for plotting-----------------

#This is the original plot from the code in the web
## plot membrane potential trace  
    def Plot(self):
        ## plot membrane potential trace  
        plot(self.time, self.Vm)
        title('Leaky Integrate-and-Fire Example')
        ylabel('Membrane Potential (V)')
        xlabel('Time (msec)')
        ylim([0,2])
        show()


