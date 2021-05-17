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
        return features

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
        liste_output = []
        for c in self.text:
            features = self.count_punctuation(c)
            features_norm = self.normalize(features, len(c))
            liste_output.append(features_norm)
        logger.debug('Creating right output')    
        return liste_output