#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 18:49:49 2021

@author: Natasha
"""
from os import path, remove  
import logging
import logging.config
from abstract_feature_class import AllFeatures
import pandas as pd

if path.isfile("logging_punct_features.log"):  
        remove("logging_punct_features.log")  
    
logger = logging.getLogger(__name__)  
logger.setLevel(logging.DEBUG)  

logger_handler = logging.FileHandler('logging_punct_features.log')  
logger_handler.setLevel(logging.DEBUG)  

logger_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
logger_handler.setFormatter(logger_formatter) 

logger.addHandler(logger_handler)  

class PunctFeatures(AllFeatures):

    def __init__(self, text):
        self.text = text

    def count_punctuation(self, text):
        features = []
        counter_commas = text.count(",")
        counter_dots = text.count(".")
        counter_question_marks = text.count("?")
        features.append(counter_commas)
        features.append(counter_dots)
        features.append(counter_question_marks)
        logger.debug('Counting punctuation feature')
        return pd.Series(features)

    @staticmethod
    def normalize(features, length):
        feature_norm = []
        for c in features:
            if length != 0:
                c = c/length
            else:
                c == 0.0
            feature_norm.append(c)
        logger.debug('Normalizing feature')    
        return feature_norm
    
    def outputter(self):
        df = self.text
        df[['number_commas', 'number_dots', "number_question_marks"]] = df['text'].apply(self.count_punctuation)
        df['text_length'] = df['text'].str.len()
        df['number_commas'] = df['number_commas'] / df['text_length']
        df['number_dots'] = df['number_dots'] / df['text_length']
        df['number_question_marks'] = df['number_question_marks'] / df['text_length']
        logger.debug('Creating data frame with features')    
        return df