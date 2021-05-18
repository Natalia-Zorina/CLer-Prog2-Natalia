#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:43:38 2021

@author: Natasha
"""

from sklearn.model_selection import train_test_split
from preprocess import preprocess

def split_data(data):
    data_train, data_test = train_test_split(data, test_size=0.2, stratify=data['label'])
    data_train, data_validate = train_test_split(data_train, test_size=0.125, stratify=data_train['label'])
    data_train.to_csv("Data_train.csv")
    data_test.to_csv("Data_test.csv")
    data_validate.to_csv("Data_validate.csv")

def main():
    
    DATAPATH = "/Users/Natasha/Универ/Sommersemester 21/irony-labeled.csv"
    data = preprocess(DATAPATH)
    split_data(data)

if __name__ == '__main__':
    main()