#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 19:36:26 2018

@author: piecia
"""

import matplotlib.pyplot as plt
import numpy as np

import importlib

     
#inhouse:

import tools as tools
importlib.reload(tools)


import tools_arrays as tools_arrays
importlib.reload(tools_arrays)
import tools_misc as tools_misc
importlib.reload(tools_misc)

CLASS_COLORS = ['black', 'red', 'orange', 'blue', 'green', 'magenta', 'yellow', 'cyan']
MARGIN_RATIO = 0.05
   

def plot_classes(data, y, numerical, labs):
    

    classes = np.sort(list(set(y)))
    classes_indexes = []
    for class_now in classes:
        classes_indexes.append(tools_arrays.indices_of_value_list(y, class_now))

    plot_classes_horisontal(data, y, classes_indexes, numerical, labs)
    
    if tools_misc.isodd(len(numerical)):
        plotsNo = len(numerical)
        add_last = True
    else:
        plotsNo = len(numerical)-1
        add_last = False

    for varNo in range(0, plotsNo, 2):
        plot_2_vars(data, y, classes_indexes, varNo, numerical, labs)
        
    if add_last:
        plot_2_vars(data, y, classes_indexes, len(numerical)-1, numerical, labs)


def plot_classes_horisontal(data, y, classes_indexes, numerical, labs):
    
      
    for varNo in numerical:
        plt.figure()
        for i, class_indexes in enumerate(classes_indexes):
            values_to_plot = tools_arrays.items_by_index(data[varNo], class_indexes)
            plt.plot(values_to_plot , 'o', color=CLASS_COLORS[i])
            plt.xlabel(labs[varNo])        


def plot_2_vars(data, y, classes_indexes, varNo, numerical, labs):
    
    plt.figure()
    for i, class_indexes in enumerate(classes_indexes):
        var1val = data[numerical[varNo]]
        var2val = data[numerical[varNo+1]]
        values_to_plot1 = tools_arrays.items_by_index(var1val, class_indexes)
        values_to_plot2 = tools_arrays.items_by_index(var2val, class_indexes)
        plt.plot(values_to_plot1, values_to_plot2, '+', color=CLASS_COLORS[i])    
        plt.xlabel(labs[numerical[varNo]])  
        plt.ylabel(labs[numerical[varNo+1]])  
        plt.axis(get_2axes_range(values_to_plot1, values_to_plot2, 0.05))


def get_2axes_range(values_x, values_y, margin_ratio):
    
    x_range = get_1axis_range(values_x)
    y_range = get_1axis_range(values_y)
    
    return x_range + y_range
     

def get_1axis_range(values_to_plot):
        
    max_val = max(values_to_plot)
    min_val = min(values_to_plot)
    margin = (max_val - min_val) * MARGIN_RATIO
    
    return [min_val - margin, max_val + margin]
        
