#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 19:32:54 2018

@author: boz
"""


import numpy as np
import copy


def find_remove_outliers(data, outliers):
    
    # remove all items without classification (output), or without any \
    # other numerical value

    outliers['all'] = copy.deepcopy(outliers['manual'])
    outliers = iterate_check_outliers(data, outliers)
    
    data, y = remove_outliers(data, outliers['all'])

    
    return data, outliers


def iterate_check_outliers(data, outliers):
    
    # data[feature][item]
    
    length = len(data[0])
    for i in range(length):
        if check_numerical_outl(data, i, outliers['numerical']) \
        and not i in outliers['all']:
            #print('dd',i)
            outliers['all'].append(i)
            
    outliers['all'] = np.sort(outliers['all'])
    
    return outliers
    
    
def check_numerical_outl(data, i, numerical):

    is_outlier = False

    for numericalhere in numerical:
        if not type(data[numericalhere][i]) == int \
        and not type(data[numericalhere][i])==float: \
            is_outlier = True    
    
    return is_outlier

    
def remove_outliers(data, outliers):
    
    # data = dict: ['feature name'][item]

    if len(outliers) > 0:
        data_clean = []
        for var in data.keys():
            for i in reversed(outliers):
                data['var'].pop(i)
            
            
    return data_clean