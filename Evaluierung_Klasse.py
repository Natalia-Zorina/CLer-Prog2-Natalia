#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 13:21:42 2021

@author: Natasha
"""
import numpy as np

class Evaluation():
    
    def __init__(self, classifier_df):
        self.classifier_df = classifier_df
        
    def evaluation_table(self, gold_daten):
        gold_daten['Classifier'] = self.classifier_df['Class']
        gold_daten['Result'] = np.where(gold_daten['Golden Class'] == gold_daten['Classifier'], 'True', 'False')
        return gold_daten
    
    def evaluation_number(self, output_df):
        true_count = output_df.loc[output_df.Result == 'True', 'Result'].count()
        evaluation_number = true_count / len(output_df.index)
        return "Accuracy = " + str(evaluation_number*100) + '%'
        
        
    def output(self, gold_daten):
        output_table = self.evaluation_table(gold_daten)
        print(output_table)
        output_number = self.evaluation_number(output_table)
        return output_number
        
        
        