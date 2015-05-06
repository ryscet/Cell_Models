# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:43:49 2015

@author: ryszardcetnarski
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from math import sqrt


class SpacePlot:
    'Draws an image in which each cell represents the spiking activity of a neuron in a population'
      
#Cell count is the total amount of cells, activity is the matrix of time series
    def __init__(self, _cellCount, _activity):
        self.cellCount =  _cellCount
        self.dimensions = int(sqrt(self.cellCount))
        self.grid = np.zeros(self.cellCount).reshape(self.dimensions,self.dimensions)
        self.fig = plt.figure()
        self.space_ax = self.fig.add_subplot(111)
        self.bp = self.space_ax.imshow(self.grid, interpolation = 'none')
        self.Vm = _activity 

##This is are the real time plots I added
##This plot should show the activity of neurons in the network (simplified to a 2d grid)


    def space_animate(self, t):
    #This function is called by the animation function in plot_activity. The iterator t is incremented by the animation function.
    #Here we take the 2D coordinates of the grid (i and j are like x and y) and assign to them a value from a matrix of activity at time t. 
    #In the matrix of activity Vm the rows represent a cell and column represent time [cell_1_t1, cell_1_t2, cell_1_t3...,
    #                                                                                  cell_2_t1, cell_2_t2, cell_2_t3..., ] 
        if(t < len(self.Vm[0])):
        #Iterate through each box of 2D grid
            for i in range(0,self.dimensions):
                for j in range(0,self.dimensions):
                #Assign corresponding activity, add the column multiplied by dimensions to the row to get a translation from a matrix of 1D timeseries to 2D spaceplot
                   #self.grid[i,j] = self.Vm[(i * self.dimensions) + j,t]
                   self.grid[i,j] = self.Vm[i,j][t]
                   print(t)
            bp = self.space_ax.imshow(self.grid, interpolation = 'none')
#            print(self.grid)
            return bp,
#HACK once animation has played stop the animation, right now it will play a dead population 
        else:
            self.grid = np.zeros(self.cellCount).reshape(self.dimensions,self.dimensions)
            bp = self.space_ax.imshow(self.grid, interpolation = 'none')
            print ("t too big")
            return bp,
            
    
    def plot_activity(self):
       anim_space = animation.FuncAnimation(self.fig,  self.space_animate, interval=500, blit=True)
#       try:
#           plt.show()
#       except AttributeError: 
#           pass
