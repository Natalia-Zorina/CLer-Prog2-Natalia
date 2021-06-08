#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:55:25 2021

@author: Natasha
"""

import pandas as pd
from feature_class_punctuation import PunctFeatures
from Word_features import count_stopwords

class Classifier():

    def __init__(self, df):
        self.df = df

    def train_model(self):
        return self.df.groupby(['label']).mean()

    def predict_model(self, train):
        #selecting columns and rows from DataFrames
        df_notironic = train.loc[:0, 'number_commas'::]
        df_ironic = train.loc[1:2, 'number_commas'::]
        self.df = self.df.loc[:, 'number_commas'::]
        #counting distance (|f1 - fd| + |f2 - fd|...)
        distanz_notironic = pd.DataFrame(abs(df_notironic.values - self.df.values), self.df.index)
        distanz_notironic = pd.DataFrame(distanz_notironic.sum(axis=1), columns = ["Class"])
        distanz_ironic = pd.DataFrame(abs(df_ironic.values - self.df.values), self.df.index)
        distanz_ironic = pd.DataFrame(distanz_ironic.sum(axis=1), columns = ["Class"])
        #selecting class with minimal distance
        df_class = distanz_ironic.gt(distanz_notironic).astype(int)
        return df_class.replace({0: "Ironic", 1: "Not Ironic"})

        
def main():

    DATAPATH = "/Users/Natasha/Library/Mobile Documents/com~apple~CloudDocs/Универ/Sommersemester 21/Prog 2/DATA/Data_train_features.csv"
    df = pd.read_csv(DATAPATH)
    train_model = Classifier(df).train_model()
    #creating dummy DataFrame
    texts = ["hello, world!","My name is Alice.","Humpty Dumpty had a great fall."]
    dummy = pd.DataFrame(texts, columns = ['text'])
    dummy_df = PunctFeatures(dummy).outputter()
    dummy_df['number_stopwords'] = dummy_df['text'].apply(count_stopwords)
    dummy_df['number_stopwords'] = dummy_df['number_stopwords'] / dummy_df['text_length']
    #calling predict_model function
    predict_model = Classifier(dummy_df).predict_model(train_model)
    print(predict_model)

if __name__ == '__main__':
    main()
