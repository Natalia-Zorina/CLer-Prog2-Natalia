#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:53:48 2021

@author: Natasha
"""
from feature_class_punctuation import PunctFeatures

def main():
    text = ["hello, world!","My name is Alice.","Humpty Dumpty had a great fall."]
    punct_features = PunctFeatures(text).count_punctuation()
    print(punct_features)

if __name__ == '__main__':
    main()