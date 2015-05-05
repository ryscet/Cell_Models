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
                #Assign corresponding activity
                   self.grid[i,j] = self.Vm[i + j,t]
                   print(self.grid)
            bp = self.space_ax.imshow(self.grid, interpolation = 'none')
            return bp,
        else:
            self.grid = np.zeros(self.cellCount).reshape(self.dimensions,self.dimensions)
            bp = self.space_ax.imshow(self.grid, interpolation = 'none')
            print ("t too big")
            return bp,
            
    
    def plot_activity(self):
       anim_space = animation.FuncAnimation(self.fig,  self.space_animate, interval=500, blit=True)
     #  anim_space = animation.FuncAnimation(self.fig,  self.space_animate, frames=30, interval=10, blit=True)
