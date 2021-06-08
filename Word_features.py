#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 12:39:44 2021

@author: Natasha
"""
import pandas as pd
from nltk.corpus import stopwords

        
def count_stopwords(text):    
    stops = stopwords.words('english')
    counter = 0
    for word in text:
        if word in stops:
            counter += 1
    return pd.Series(counter)