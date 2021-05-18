#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:25:43 2021

@author: Natasha
"""
import pandas as pd

def preprocess(data):
    df = pd.read_csv(data)
    df = df.rename(columns={'comment_text': 'text'})
    df = df.rename_axis("ID")
    df = df.drop_duplicates()
    filter = df['text'] != ''
    df = df[filter]
    return df