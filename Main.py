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
import LinearNeuron as ln


simulationTime = 1000 # in msec (simulated msec)
firingRate = 100 # Spikes per second, parameter for random spike 

neuronsCount = 64 #Has to have a integer square root, i.e. a square matrix 3X3, 4x4...
matrixDim = int(sqrt(neuronsCount))
#Already start with populations arranged in a 2D matrix, because then connections are easy (only multiply the output matrix by connectivity matrix). To simulate activity flatten can be used. 
pre_synaptic_population = np.empty((matrixDim,matrixDim), dtype=object)
post_synaptic_population = np.empty((matrixDim,matrixDim), dtype=object)

#Now I have to declare object type as dtype, but in this case these are numpy arrays we are putting there, perhaps this can be faster
allOutput= np.empty((matrixDim,matrixDim), dtype=object)
allPost= np.empty((matrixDim,matrixDim), dtype=object)


def connectivityMatrix(_matrixDim):
    connections = np.zeros([_matrixDim, _matrixDim])
    for i in range(0, _matrixDim):
        for j in range(0, _matrixDim):
            if(i == j):
                connections[i,j] = 1.0
    return connections
connections = connectivityMatrix(neuronsCount)

#Create the post synaptic, i.e. receiving population
for i in range (0,matrixDim):
    for j in range (0,matrixDim):
        pre_synaptic_population[i,j] = rs.RandomSpike(firingRate)
        post_synaptic_population[i,j] = myLif.IntegrateFire()
#        post_synaptic_population[i,j] = ln.LinearNeuron()

#This just to make a copy of pre_synaptic Vm and put it in a variable
for i in range (0,matrixDim):
    for j in range (0,matrixDim):
        allOutput[i,j] = pre_synaptic_population[i,j].Vm

#Main simulation
for t in range(1, simulationTime):        
    for i in range (0,int(sqrt(neuronsCount))):
        for j in range (0,int(sqrt(neuronsCount))):
             post_synaptic_population[i,j].Simulate(t, allOutput[i,j][t] * connections[(i*matrixDim) + j, (i*matrixDim) + j]) 
#             post_synaptic_population[i,j].Simulate(t, 5) 

#[neuron.Plot() for neuron in pre_synaptic_population.flatten()]
#[neuron.Plot() for neuron in post_synaptic_population.flatten()]


#Replay the activity on a futuristic space plot       
pre_SpacePlot = myPlt.SpacePlot(neuronsCount, allOutput)
pre_SpacePlot.plot_activity()

#This just to make a copy of post_synaptic Vm and put it in a variable
for i in range (0,matrixDim):
    for j in range (0,matrixDim):
        allPost[i,j] = post_synaptic_population[i,j].Vm

post_SpacePlot = myPlt.SpacePlot(neuronsCount, allPost)
post_SpacePlot.plot_activity()


