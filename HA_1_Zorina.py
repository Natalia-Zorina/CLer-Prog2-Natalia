#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 18:49:49 2021

@author: Natasha
"""
class Ironic: 
    
    def __init__(self, text):
        self.text = text.split("'")
        for c in self.text:
            if c == '[' or ']' or ',':
                self.text.remove(c)
        
        
    def count_punctuation(self):
        liste_output = []
        for c in self.text:
            counter_commas = c.count(",")
            counter_dots = c.count(".")
            counter_question_marks = c.count("?")
            normalisiert_commas = counter_commas / len(c)
            normalisiert_dots = counter_dots / len(c)
            normalisiert_question = counter_question_marks / len(c)
            liste_output.append([normalisiert_commas, normalisiert_dots, normalisiert_question])
        return liste_output
        
        
        
def main():
    text = input()
    liste = Ironic(text)
    print(liste.count_punctuation())
    
if __name__ == '__main__':
    main()   