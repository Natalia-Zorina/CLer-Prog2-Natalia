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
        self.B = PunctFeatures(["","My name is Alice.",".,."])

    def test_count_punctuation(self):
        self.assertEqual(self.A.count_punctuation("hello, world!"), [1, 0, 0])
        self.assertEqual(self.A.count_punctuation("My name is Alice."), [0, 1, 0])
        self.assertEqual(self.A.count_punctuation("Humpty Dumpty had a great fall."), [0, 1, 0])
        self.assertEqual(self.A.count_punctuation(".,."), [1, 2, 0])
        self.assertEqual(self.A.count_punctuation(""), [0, 0, 0])
        self.assertEqual(self.A.count_punctuation("HELLO?.,."), [1, 2, 1])

    def test_normalize(self):
        self.assertEqual(PunctFeatures.normalize([1, 0, 0], 13), [0.07692307692307693, 0.0, 0.0])
        self.assertEqual(PunctFeatures.normalize([0, 1, 0], 17), [0.0, 0.058823529411764705, 0.0])
        self.assertEqual(PunctFeatures.normalize([0, 1, 0], 31), [0.0, 0.03225806451612903, 0.0])
        self.assertEqual(PunctFeatures.normalize([10, 10, 10], 10), [1.0, 1.0, 1.0])
        self.assertEqual(PunctFeatures.normalize([0, 0, 0], 0), [0.0, 0.0, 0.0])
    
    def test_outputter(self):
        self.assertEqual(self.A.outputter(), [[0.07692307692307693, 0.0, 0.0], [0.0, 0.058823529411764705, 0.0], [0.0, 0.03225806451612903, 0.0]])    
        self.assertEqual(self.B.outputter(), [[0.0, 0.0, 0.0], [0.0, 0.058823529411764705, 0.0], [0.3333333333333333, 0.6666666666666666, 0.0]])    

"""
class TestClassifier(unittest.TestCase):

    def setUp(self):
        self.A = Classifier("Because the Reddit Liberal Brigade™ would downvote it to oblivion within minutes? Does that sound about right?", [[0.0, 0.0, 0.01818181818181818]])
        self.B = Classifier("Would he win?", [[0.0, 0.0, 0.07692307692307693]])
        self.C = Classifier("", [[0.0, 0.0, 0.0]])
        self.D = Classifier("Insane like a fox. Ted Cruz is actually very very intelligent. It's his constituents that are insane. He's just playing the part.", [[0.0, 0.031007751937984496, 0.0]])
        self.E = Classifier("Yeah I didn't get far. This article fills me with sadness", [[0.0, 0.017543859649122806, 0.0]])

    def test_create_model(self):
        self.assertEqual(self.A.create_model(), [[0.0, 0.0, 0.01818181818181818]])
        self.assertEqual(self.B.create_model(), [[0.0, 0.0, 0.07692307692307693]])
        self.assertEqual(self.C.create_model(), "invalid input")
        
           Input:   Statistik der Ironic / Nicht-Ironic Klassen in einem CSV Format
           (Strings mit Features und ihrer Zugehörigkeit zu der Ironic / Nicht-Ironic Klasse)
           Output:  Ein Model mit representativen Features der Ironic / Nicht-Ironic Klassen
           Mögliche Testinputs: 1) Ein Ironic String und Features
                                2) Ein Nicht-Ironic String und Features 
                                3) Ein leerer String
    
    def test_classifier(self):
        self.assertEqual(self.D.classifier([[0.0, 0.0, 0.01818181818181818]], [[0.0, 0.0, 0.07692307692307693]]), "Ironic")
        self.assertEqual(self.E.classifier([[0.0, 0.0, 0.01818181818181818]], [[0.0, 0.0, 0.07692307692307693]]), "Not-Ironic")
        self.assertEqual(self.C.classifier([[0.0, 0.0, 0.01818181818181818]], [[0.0, 0.0, 0.07692307692307693]]), "invalid input")
        
           Input:   Neue Strings + Features, representative Features für beide Klassen
           Output:  Zugehörigkeit der Strings zu einer der Klassen anhand des Modells
           Mögliche Testinputs: 1) Ein Ironic String + Features + representative Features für beide Klassen
                                2) Ein Nicht-Ironic String + Features + representative Features für beide Klassen
                                3) Ein leerer String + Features + representative Features für beide Klassen
        
    def test_evaluierung(self):
        self.assertEqual(Classifier.evaluierung("Insane like a fox. Ted Cruz is actually very very intelligent. It's his constituents that are insane. He's just playing the part.", "Ironic", "Ironic"), "100%")
        self.assertEqual(Classifier.evaluierung("Yeah I didn't get far. This article fills me with sadness", "Not-Ironic", "Not-Ironic"), "100%")
        self.assertEqual(Classifier.evaluierung("", "Not-Ironic", "Not-Ironic"), "invalid Input")
        
           Input:   Unsere Prognose + "Gold class"
           Output:  Prozent der Präzision des Modells 
           Mögliche Testinputs: 1) Ironic String + Zugehörigkeit anhand des Modells + Zugehörigkeit anhand der Golden Klasse
                                2) Nicht-Ironic String + Zugehörigkeit anhand des Modells + Zugehörigkeit anhand der Golden Klasse
                                3) Ein leerer String 
"""    
        

if __name__ == '__main__':
    unittest.main()