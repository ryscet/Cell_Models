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
      
    ## setup parameters and state variables
    T = 1000                # total time to simulate (msec)
    ## Random Spike variables
    spike_amp = 1.5

    def __init__(self, _firingRate):
        self.Vm = np.zeros(self.T) # potential (V) trace over time 
        self.firingRate =  _firingRate
        self.spike_t = sample(range(0, self.T), self.firingRate) # select a random index for a spike. Firing rate determines the amount of spike within the simulation time. They are uniformely distributed.
        self.Vm[self.spike_t] = self.spike_amp # At the selected random indexes mark a spike



    #def Simulate(self, timestep):        
        #return self.Vm

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
