#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:53:48 2021

@author: Natasha
"""
from os import path, remove
import pandas as pd
import logging
import logging.config
from feature_class_punctuation import PunctFeatures

def main():
    if path.isfile("logging_classify.log"):  
        remove("logging_classify.log")  
    
    logger = logging.getLogger(__name__)  
    logger.setLevel(logging.DEBUG)  
    
    logger_handler = logging.FileHandler('logging_classify.log')  
    logger_handler.setLevel(logging.DEBUG)  
    
    logger_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
    logger_handler.setFormatter(logger_formatter) 
    
    logger.addHandler(logger_handler)  
    
    text = ["hello, world!","My name is Alice.","Humpty Dumpty had a great fall."]
    data_frame = pd.DataFrame(text, columns=['text'])
    punct_features = PunctFeatures(data_frame).outputter()
    punct_features.to_csv("PunctFeatures.csv")
    logger.debug(punct_features)

if __name__ == '__main__':
    main()
