# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:24:16 2015

@author: ryszardcetnarski
"""

import Random_Spike as rs
import Plotting as myPlt
import numpy as np
import lif as myLif
from math import sqrt


simulationTime = 1000 # in msec (simulated msec)
firingRate = 100 # Spikes per second, parameter for random spike 

neuronsCount = 16 #Has to have a integer square root, i.e. a square matrix 3X3, 4x4...
matrixDim = int(sqrt(neuronsCount))
#Already start with populations arranged in a 2D matrix, because then connections are easy (only multiply the output matrix by connectivity matrix). To simulate activity flatten can be used. 
pre_synaptic_population = np.empty((matrixDim,matrixDim), dtype=object)
post_synaptic_population = np.empty((matrixDim,matrixDim), dtype=object)

#Now I have to declare object type as dtype, but in this case these are numpy arrays we are putting there, perhaps this can be faster
allOutput= np.empty((matrixDim,matrixDim), dtype=object)


#Create the post synaptic, i.e. receiving population
for i in range (0,matrixDim):
    for j in range (0,matrixDim):
        pre_synaptic_population[i,j] = rs.RandomSpike(firingRate)
        post_synaptic_population[i,j] = myLif.IntegrateFire()

#[neuron.Plot() for neuron in pre_synaptic_population.flatten()]
for i in range (0,int(sqrt(neuronsCount))):
    for j in range (0,int(sqrt(neuronsCount))):
        allOutput[i,j] = pre_synaptic_population[i,j].Vm


#Replay the activity on a futuristic space plot       
mySpacePlot = myPlt.SpacePlot(neuronsCount, allOutput)
mySpacePlot.plot_activity()

#for t in range(1,simulationTime):        
#    [neuron.Simulate() for neuron in post_synaptic_population]
#    
#for i in range(1,simulationTime):
#    activity = pre_neuron.Simulate(i, np.random.uniform(0.5,1.5))
#    post_neuron.Simulate(i, activity)
#    if(i >= simulationTime - 1):
#        post_neuron.Plot()
#        pre_neuron.Plot()
#
#def connectivityMatrix(_neuronsCount):
#    connections = np.zeros([_neuronsCount, _neuronsCount])
#    for i in range(0, _neuronsCount):
#        for j in range(0, _neuronsCount):
#            if(i == j):
#                connections[i,j] = 1.0
#    return connections
#
#
#
#pre_neuron = myLif.IntegrateFire()
#post_neuron = myLif.IntegrateFire()
    
    
    #Hack putting different inputs for LIF neurons so they can be plotted. Otherwise their activity is the same and therefore the plot is all one color and nothing is vivible.

#for i in range (0,4):
##To change neuron type swap the myLif.IntegrateFire() for rs.RandomSpike(firingRate)
#    input_arr.append(np.random.uniform(1,3.5))
#    allNeurons.append(myLif.IntegrateFire(input_arr[i]))

#Record the activity of all neurons and store them in an array
#for neuron in allNeurons:
#    activity = neuron.Simulate()
#    allActivity.append(activity)
#allActivity = np.array(allActivity)

#

#
#mySpacePlot.plot_activity()


