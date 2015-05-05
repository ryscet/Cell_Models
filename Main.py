# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:24:16 2015

@author: ryszardcetnarski
"""

import Random_Spike as rs
import Plotting as myPlt
import numpy as np

#myNeuron = rs.RandomSpike(60)
#
#activity = myNeuron.Simulate()
#myNeuron.Plot(activity)


tmpData = np.array([[10,20,30,40,50,60,70,80,90,100], [10,9,8,7,6,5,4,3,2,1],[1,2,3,4,5,6,7,8,9,10], [10,9,8,7,6,5,4,3,2,1]])

mySpacePlot = myPlt.SpacePlot(4, tmpData)

mySpacePlot.plot_activity()