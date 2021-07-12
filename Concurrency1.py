#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 13:10:45 2021

@author: Natasha
"""

# Mein Computer arbeitet mit 2 Kernen
# Dieser Code hat folgende Ergebnisse: 6,64s user 1,77s system 144% cpu 5,797 total
# Der Code ohne Concurrency hat diese Ergebnisse: 1,35s user 0,23s system 103% cpu 1,531 total

import nltk 
import pandas as pd
import multiprocessing as mp


def pos_tags(list_text):
    return nltk.pos_tag(list_text)
    
    
if __name__ == '__main__':
    DATA = '/Users/Natasha/Library/Mobile Documents/com~apple~CloudDocs/Универ/Sommersemester 21/Prog 2/DATA/Data_train.csv'
    df = pd.read_csv(DATA)
    list_text = df['text'].to_list()
    with mp.Pool() as pool:
        pool.map(pos_tags, [list_text])