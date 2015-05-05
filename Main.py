# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:24:16 2015

@author: ryszardcetnarski
"""

import Random_Spike as rs
import Plotting as myPlt
import numpy as np

allNeurons = []
allActivity = []
for i in range (0,4):
    print(i)
    allNeurons.append(rs.RandomSpike(200))

for neuron in allNeurons:
    activity = neuron.Simulate()
    allActivity.append(activity)
allActivity = np.array(allActivity)


        
mySpacePlot = myPlt.SpacePlot(len(allActivity), allActivity)

mySpacePlot.plot_activity()