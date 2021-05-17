#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 14:29:49 2021

@author: Natasha
"""

import unittest
from feature_class_punctuation import PunctFeatures

class TestPunctFeaturesMethods(unittest.TestCase):

    def setUp(self):
        self.A = PunctFeatures(["hello, world!","My name is Alice.","Humpty Dumpty had a great fall."])

    def test_count_punctuation(self):
        self.assertEqual(self.A.count_punctuation("hello, world!"), [1, 0, 0])

    def test_normalize(self):
        self.assertEqual(PunctFeatures.normalize([1, 0, 0], 13), [0.07692307692307693, 0.0, 0.0])
        self.assertEqual(PunctFeatures.normalize([0, 0, 0], 0), [0.0, 0.0, 0.0])
    
    def test_outputter(self):
        self.assertEqual(self.A.outputter(), [[0.07692307692307693, 0.0, 0.0], [0.0, 0.058823529411764705, 0.0], [0.0, 0.03225806451612903, 0.0]])    

if __name__ == '__main__':
    unittest.main()