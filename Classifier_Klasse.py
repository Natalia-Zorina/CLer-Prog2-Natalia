#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:55:25 2021

@author: Natasha
"""

import pandas as pd
import click
from feature_class_punctuation import PunctFeatures
from Word_features import count_stopwords
from exceptions import FeatureException
from exceptions import InputException
from Evaluierung_Klasse import Evaluation
import warnings

class Classifier():

    def __init__(self, df):
        self.df = df

    def train_model(self, features_for_train):  
        
        ''' 
        Zeit-Komplexität für diese Schleife ist O(max(N, M)))
        Diese Schleife prüft, ob die von User gegebenen Features zugänglich
        und schon berechnet sind. Wenn nicht, wirft die Schleife einen Fehler.
        Die Schleife erstellt eine neue Liste mit zugänglichen Feautres. 
        Man kann anstatt dieser Liste einen Generator benutzen,
        um die Memory zu sparren. 
        '''
        
        list_user_features = []
        for c in features_for_train:
            if c not in list(self.df.columns)[1:]:
                raise FeatureException(str(c) + " feature is not available")
            else:
                list_user_features.append(c)
        if "label" in list_user_features:
            self.df = self.df[list_user_features]
        else:
            list_user_features.append("label")
            self.df = self.df[list_user_features]
        return self.df.groupby(['label']).mean()

    def predict_model(self, train):
        for c in list(train.columns):
            if c not in list(self.df.columns):
                warnings.warn(str(c) + " feature is not available in test data")
                train = train.drop(columns = c) 
        # selecting columns and rows from DataFrames
        df_notironic = train.loc[:0]
        df_ironic = train.loc[1:2]     
        self.df = self.df[list(train.columns)]
        # counting distance (|f1 - fd| + |f2 - fd|...)
        distanz_notironic = pd.DataFrame(abs(df_notironic.values - self.df.values), self.df.index)
        distanz_notironic = pd.DataFrame(distanz_notironic.sum(axis=1), columns = ["Class"])
        distanz_ironic = pd.DataFrame(abs(df_ironic.values - self.df.values), self.df.index)
        distanz_ironic = pd.DataFrame(distanz_ironic.sum(axis=1), columns = ["Class"])
        # selecting class with minimal distance
        df_class = distanz_ironic.gt(distanz_notironic).astype(int)
        return df_class.replace({0: "Ironic", 1: "Not Ironic"})

@click.command()
@click.argument('data', required=True)

def main(data):

    df = pd.read_csv(data)
    print("Available features: ", list(df.columns)[1:])
    features_for_train = input("Please enter features for model training by whitespace without quotes and commas: ")
    if type(features_for_train) != str:
        raise InputException(str(features_for_train) + " is not a string")
    train_model = Classifier(df).train_model(features_for_train.split())
    # creating dummy DataFrame
    texts = ["hello, world!","My name is Natalia.","I'm 21 years old."]
    dummy = pd.DataFrame(texts, columns = ['text'])
    dummy_df = PunctFeatures(dummy).outputter()
    dummy_df['number_stopwords'] = dummy_df['text'].apply(count_stopwords)
    dummy_df['number_stopwords'] = dummy_df['number_stopwords'] / dummy_df['text_length']
    #calling predict_model function
    predict_model = Classifier(dummy_df).predict_model(train_model)
    gold_class = "Not Ironic", "Not Ironic", "Not Ironic"
    gold_daten = pd.DataFrame(gold_class, columns = ['Golden Class'])
    evaluation_daten = Evaluation(predict_model).output(gold_daten)
    print(evaluation_daten)

if __name__ == '__main__':
    main()
