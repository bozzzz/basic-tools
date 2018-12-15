#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:59:09 2018

@author: piecia
"""

import random 
import importlib
    
#in house github:

#import tools
#importlib.reload(tools)
import tools_arrays
importlib.reload(tools_arrays)



def divide_train_test(validation, length):
    
    if validation['type'] =='random':
        validation['train'] = random.sample(range(length), \
                  int(length*validation['percent_train']/100)) #
        # randit gives repetitions which gives problems with exracting train test:
        #np.random.randint(low=0, high=length, size=int(length*percent/100))
        validation['train'].sort() 
    
    validation['test'] = list(range(0,length))
    for i in validation['train'][::-1]:
        validation['test'].pop(i) # works since index=number!
        
        
    return validation


def get_train_test_data(validation, data):
    
    
    data_train = []
    data_test = []
    for var in data:
        data_train.append(tools_arrays.items_by_index(var, validation['train']))        
        data_test.append(tools_arrays.items_by_index(var, validation['test']))
        
    data_split = {
              'data_train': data_train
            , 'data_test' : data_test
            }
        
    return data_split