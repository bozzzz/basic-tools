#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 10:34:58 2018

@author: boz
"""

import numpy as np

import nltk
from nltk.stem.lancaster import LancasterStemmer


def get_class_array(y):
        
    ''' get groung truth in y, output array with  '0' for each class and '1' for current class 
    '''
    # todo: in work code standardise data and use this one instead of make_ground_truth

    print('----preprocessing, get_class_array')
    class_array_full = []
    classes = np.sort(list(set(y)))
    class_array_empty = [0] * len(classes)
    
    for class_now in enumerate(y):
        # '0' for each tag and '1' for current tag
        class_array = list(class_array_empty)        
        class_array[classes.index(class_now)] = 1
        class_array_full.append(class_array)
           
    return class_array_full


def get_features_intermediate(data):
    
    
    data['description words'] = []
    for item in data['description']:
        data['description words'].append(nltk.word_tokenize(item))
    
    
    return data


def list_words(words):
    
    ''' list words in all wwws '''
    stemmer = LancasterStemmer()
    words = []
    ignore_words = ['?']   
    
    for i, item in enumerate(words):
        
        if np.mod(i, 20) == 0:
            print('---stemmed ', i, 'from ', len(words))
        words.extend(item)

    stemmed_words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
    unique_stemmed_words = list(set(stemmed_words))    
    
    return unique_stemmed_words

    
def tokenize_data(words, unique_stemmed_words):

    # unchanged
    stemmer = LancasterStemmer()
    # create our training data
    tokenized_train_data = []

    # training set, bag of words for each text
    for i, item in enumerate(words):
        # initialize our bag of words
        if np.mod(i, 20) == 0:
            print('---tokenized ', i, 'from ', len(words))
        bag = []
        pattern_words = [stemmer.stem(word.lower()) for word in item]
        # create our bag of words array
        for w in unique_stemmed_words:
            bag.append(1) if w in pattern_words else bag.append(0)
    
        tokenized_train_data.append(bag)
        
    return tokenized_train_data
        