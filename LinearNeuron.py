# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:51:41 2015

@author: ryszardcetnarski
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:11:54 2015

@author: ryszardcetnarski
"""
import numpy as np
from pylab import *

class LinearNeuron:
    'Just follows the activity in the presynaptic neuron, used for debugging connections'
      
    ## setup parameters and state variables
    T = 1000                # total time to simulate (msec)

    def __init__(self, ):
        self.Vm = np.zeros(self.T) # potential (V) trace over time 

    def Simulate(self, timestep, _input):        
        self.Vm[timestep] = _input
        return self.Vm[timestep]

    def Plot(self):
        ## plot membrane potential trace
        figure()
        time = np.linspace(0,self.T,1000)  
        plot(time, self.Vm)
        title('Random Spike')
        ylabel('Membrane Potential (V)')
        xlabel('Time (msec)')
        ylim([0,2])
        show()
