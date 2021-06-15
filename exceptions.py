#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 12:43:52 2021

@author: Natasha
"""

class FeatureException(Exception):
    def __init__(self, msg):
        self.msg = msg


class InputException(Exception):
    def __init__(self, msg):
        self.msg = msg