#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 18:49:49 2021

@author: Natasha
"""
from abstract_feature_class import AllFeatures

class PunctFeatures(AllFeatures):

    def __init__(self, text):
        self.text = text

    def count_punctuation(self):
        liste_output = []
        for c in self.text:
            features = []
            counter_commas = c.count(",")
            counter_dots = c.count(".")
            counter_question_marks = c.count("?")
            features.append(counter_commas)
            features.append(counter_dots)
            features.append(counter_question_marks)
            features_norm = self.normalize(features, len(c))
            liste_output.append(features_norm)
        return liste_output

    @staticmethod
    def normalize(features, length):
        feature_norm = []
        for c in features:
            c = c/length
            feature_norm.append(c)
        return feature_norm