#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 13:10:45 2021

@author: Natasha
"""

# Mein Computer arbeitet mit 2 Kernen

import nltk 
import pandas as pd


def pos_tags(list_text):
    return nltk.pos_tag(list_text)
    
    
if __name__ == '__main__':
    DATA = '/Users/Natasha/Library/Mobile Documents/com~apple~CloudDocs/Универ/Sommersemester 21/Prog 2/DATA/Data_train.csv'
    df = pd.read_csv(DATA)
    list_text = df['text'].to_list()
    pos_tags(list_text)