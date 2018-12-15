#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:52:58 2018

@author: bozzzz
"""

import pandas as pd
import pandas as pd
import numpy as np
from operator import itemgetter



def sort_data_by_one_col(data, sort_by):
    
    data_sorted = []
    sort_order = np.argsort(data[sort_by])
    
    for i in range(len(data)):
#        data_sorted.append([col for _,col in sorted(zip(data[sort_by],col))]) works not for int and str zipped
        data_sorted.append(itemgetter(*sort_order)(data[i]))
        
    return data_sorted


def items_by_index(list_in, indexes):
    
    return [list_in[i] for i in indexes]


def nonrepetitive_list(list_in):
    
    return list(set(list_in))


def indices_of_value_list(list_in, value_in):
    
    return [i for i, value in enumerate(list_in) if value==value_in]


def list_into_dict(data, labs):
    
    
    data_dict = {}
    
    for i, lab in enumerate(labs):
        data_dict[lab] = data[i]
    
    return data_dict
