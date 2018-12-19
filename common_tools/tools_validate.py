#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:59:09 2018

@author: piecia
"""

import random 
import importlib
import numpy as np

#in house github:

#import tools
#importlib.reload(tools)
import tools_arrays
importlib.reload(tools_arrays)



def divide_train_test(validation, length):
    
    if validation['type'] =='random':       
        validation['test'] = get_test_random(validation, validation['length'])
        
    elif validation['type'] =='multilabel':
        validation['test'] = get_test_multilab(validation)
    
    validation['train'] = get_train_from_test(validation['test'], length)
        
    return validation


def get_train_from_test(test, length):


    train = list(range(0,length))
    for i in test[::-1]:
        train.pop(i) # works since index=number!
        
    return train
    
    

def get_test_random(validation, length):
    
    test = random.sample(range(length), int(length*validation['percent_test']/100)) 
        # randit gives repetitions which gives problems with exracting train test:
        #np.random.randint(low=0, high=length, size=int(length*percent/100))
    test.sort() 
        
    return test
       
    
def get_test_multilab(validation):
    
    # divide making sure that:
    # each class is represented in the test set and training set
    # => in the test set there is at least one item for each label => this gives 30 items! (there are repetitions)
    labs = validation['labs']
    classes_list = validation['classes_list']
    test_size = int(len(labs)*validation['percent_test']/100)
    
    test = get_test_percent_each_class(validation, labs, classes_list)
    
    if len(test) > test_size: 
        test = remove_frequent_classes(test, classes_list, len(test) - test_size)
    elif len(test) < test_size:
        # now we have all classes, in test set, is it enough?
        train = get_train_from_test(test, len(labs))
        add_to_test = random.sample(train, test_size - len(test)) 
        test = test + add_to_test
        
    test = list(np.sort(test))


    return test    
          

def get_test_percent_each_class(validation, labs, classes_list):
    
    test = []
    for class_now in classes_list:
        # for each class get in-class number of test samples equalling validation['percent_test']
        items_in_class = tools_arrays.indices_of_value_list2dim(labs, class_now)
        test_in_class_idx = get_test_random(validation, len(items_in_class))
        test_in_class = tools_arrays.items_by_index(items_in_class, test_in_class_idx)
        # test_in_class - indices of items from this class in the test set, must go to test set
        test += test_in_class
        
    test = set(test)        
    test = list(np.sort(list(set(test))))
    
    return test


def remove_frequent_classes(test, classes_list, removeNo):
    
    print('No way, no coding after 7pm! fuck you')
    assert(False)
    classes_present = []
    for i in test:
        classes_present += classes_list[i]
        
    classes_present = np.sort(classes_present)
    
    
    
    return test


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