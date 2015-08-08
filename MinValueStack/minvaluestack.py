#!/usr/bin/env python
#title           :  minvaluestack.py
#description     :  This will create a header for a python script.
#author          :  Mira Mollar
#date            :  August 7, 2015
#version         :  1.0
#usage           :  python minvaluestack.py
#notes           :  This script is a practice problem for learning python :)
#                   This file will implement a stack which keeps track of its
#                   minimum value.
#python_version  :  2.7

class MinValue():

    def __init__(self, item):
        self.myList = []
        self.mins = []

    def pop(self, item):
        if item > self.mins.pop():
            self.mins.append(item)

    def push(self, add, list):


    def minimum(self, item):
        self.myList = item
        index = 0
        
        for item in self.myList:
            if item > index:
                myList
    def tests(self):
        print "+++++++++++ Test 1: Example Case from Brainstorming ++++++++++"

        thisList = [1 ,2 ,3,4]

        print "push(4, thisList)"


if __name__ == '__main__':

    MinValue().tests()
