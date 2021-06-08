#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 19:20:20 2021

@author: Natasha
"""
import csv

class DataIterator:

    def __init__(self, data, max_repeats):
        self.data = data
        self.i = 0
        self.max_repeats = max_repeats
        self.reader = csv.DictReader(open(self.data, mode='r'))

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.max_repeats:
            raise StopIteration()
        for line in self.reader:
            i = self.i
            self.i += 1
            return (i, line.get("comment_text"), line.get("label"))

    def generator(self):
        with open(self.data, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            c = 0
            for row in reader:
                yield (c, row.get("comment_text"), row.get("label"))
                c += 1


def main():

    DATAPATH = "/Users/Natasha/Универ/Sommersemester 21/irony-labeled.csv"
    data_iterator = DataIterator(DATAPATH, 10)

    i = iter(data_iterator)
    print(next(i))
    print(next(i))
    print(next(i))

    g = data_iterator.generator()
    print(next(g))
    print(next(g))
    print(next(g))


if __name__ == '__main__':
    main()