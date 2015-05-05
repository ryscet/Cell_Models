# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:11:54 2015

@author: ryszardcetnarski
"""
import numpy as np
from pylab import *
from random import sample

class RandomSpike:
    'Generates spikes in a given frequency with uniform noise'
    randomCellCount = 0
      
    ## setup parameters and state variables
    T = 1000                # total time to simulate (msec)
    ## Random Spike variables
    Vm = np.zeros(T) # potential (V) trace over time 
    spike_amp = 1.5

    def __init__(self, _firingRate):
        self.firingRate =  _firingRate
        Random_Spike.randomCellCount += 1

    def Simulate(self):        
        spike_t = sample(range(0, self.T), self.firingRate)
        self.Vm[spike_t] = self.spike_amp
        return self.Vm

    def Plot(self,activity):
        ## plot membrane potential trace
        time = np.linspace(0,self.T,1000)
  
        plot(time, activity)
        title('Random Spike')
        ylabel('Membrane Potential (V)')
        xlabel('Time (msec)')
        ylim([0,2])
        show()
