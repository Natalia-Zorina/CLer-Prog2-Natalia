#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:46:40 2021

@author: Natasha
"""

from abc import ABC, abstractmethod


class AllFeatures(ABC):

    @abstractmethod
    def normalize(self):
        pass