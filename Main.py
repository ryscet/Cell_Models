# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:24:16 2015

@author: ryszardcetnarski
"""

import Random_Spike as rs
import Plotting as myPlt
import numpy as np
import lif as myLif

#tmp = myLif.IntegrateFire()
#
#tmp.Simulate()
#tmp.Plot()

allNeurons = []
allActivity = []

#Hack putting different inputs for LIF neurons so they can be plotted. Otherwise their activity is the same and therefore the plot is all one color and nothing is vivible.
input_arr = [1.5, 2.0, 2.5, 3.0]
firingRate = 200

for i in range (0,4):
    print(i)
#To change neuron type swap the myLif.IntegrateFire() for rs.RandomSpike(firingRate)
    allNeurons.append(myLif.IntegrateFire(input_arr[i]))

for neuron in allNeurons:
    activity = neuron.Simulate()
    allActivity.append(activity)
allActivity = np.array(allActivity)


        
mySpacePlot = myPlt.SpacePlot(len(allActivity), allActivity)

mySpacePlot.plot_activity()