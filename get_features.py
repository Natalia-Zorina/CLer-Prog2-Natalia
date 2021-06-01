#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:43:56 2021

@author: Natasha
"""

import pandas as pd
from feature_class_punctuation import PunctFeatures

def main():
    
    DATAPATH = "/Users/Natasha/Library/Mobile Documents/com~apple~CloudDocs/Универ/Sommersemester 21/Prog 2/DATA/Data_train.csv"
    df = pd.read_csv(DATAPATH, usecols=('ID', 'text', 'label'))
    data_with_features = PunctFeatures(df).outputter()
    data_with_features.to_csv("Data_train_features.csv")

if __name__ == '__main__':
    main()
