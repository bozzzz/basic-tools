#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:24:12 2018

@author: boz github
"""

import xlrd
import os
import pickle
import datetime
import re

import pandas as pd


def read_xls_bycol(xls_path, sheet_name, cols):
    
    workbook = xlrd.open_workbook(xls_path)
    worksheet = workbook.sheet_by_name(sheet_name)
    
    data = []
    for col in cols:
        data.append(worksheet.col_values(col))
        
    return data


def read_xls_pandas(xls_path, sheet):
    
    df = pd.read_excel(xls_path, sheet)
    
    return df



def read_xls(xls_path, sheet_name, rows, cols):
    
    workbook = xlrd.open_workbook(xls_path)
    worksheet = workbook.sheet_by_name(sheet_name)
    #worksheet = workbook.sheet_by_index(0)
    
    data = []
    for row in rows:
        rowhere = []
        for col in cols:
            rowhere.append(worksheet.cell(row,col).value)
        data.append(rowhere)
        
    return data


def pickleit(globals_, path_pickle, comment = False, protocol = 4):
    
    
    if comment:
        print ('----Pickling: ', path_pickle)
        
    if not os.path.isdir(os.path.dirname(path_pickle)):
        os.mkdir(os.path.dirname(path_pickle))
               
    with open(path_pickle, 'wb') as f:
        pickle.dump(globals_, f, protocol = protocol)
  

def pickle_dated(globals_, path_pickle, printit = False, protocol = 4):

    date = '_' + datetime.datetime.today().strftime('%Y-%m-%d')
    path_pickle = path_pickle.replace('.', date + '.')
    pickleit(globals_, path_pickle, printit, protocol)      
    
        
def unpickleit(path1):

# using:    
#    pickled = self.unpickle(filename) 
#    for name in data.keys():
#        globals()[name] = pickled[name]

    print ('----Unpickling.... ', path1)
    with open(path1, 'rb') as f:
        data = pickle.load(f)
    print ('----Done.' )
        
    return data

    
def get_last_pickle_name(path):
    
    # name: raw_data_2018-11-13_.pickled
    REGEX_DATE = '(\d{4}[-\_\s./](\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[-\_\s./]\d{2,4})'
    # d{4} => 4 digit year, 2018, -\_\ => use _ or -

    file_names = []
    file_dates = []
    for file in files_in_folder(path):
        if 'pickle' in file:
            file_names.append(file)
            file_dates.append(re.search(REGEX_DATE, file).group(1))
            
    last_date = sorted(file_dates, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))[-1]
    
    for file in file_names:
        if last_date in file:
            last_pickle_filename = file
            
    
    return last_pickle_filename



def files_in_folder(path_folder):
    
    
    return [file for file in os.listdir(path_folder) \
            if os.path.isfile(os.path.join(path_folder, file))]
