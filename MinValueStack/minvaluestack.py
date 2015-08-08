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

    def __init__(self):
        self.myList = []
        self.mins = []

    def pop(self, item):
        if item > self.mins.pop():
            self.mins.append(item)

    def push(self, add, list):
        return "testing"


    def minimum(self, item):
        self.myList = item
        print "self.myList = " + str(self.myList)
        min = self.myList[0]

        for item in self.myList:
            print "item = " + str(item)
            if item < min:
                min = item
                print "min = " + str(min)

        self.mins.append(min)
        return min


    def tests(self):
        print "+++++++++++ Test 1: Example Cases from Brainstorming ++++++++++"

        print "thisList = [1 ,2 ,3,4]"
        thisList = [1 ,2 ,3,4]

        print "minimum(thisList)"
        minimumValue = self.minimum(thisList)

        print "Minimum Value = " + str(minimumValue)

        print "thisList = [4 ,3 ,2 ,1]"
        thisList = [4 ,3 ,2 ,1]

        print "minimum(thisList)"
        minimumValue = self.minimum(thisList)

        print "Minimum Value = " + str(minimumValue)

        print "+++++++++++++++++ Test 2: Float Data Type +++++++++++++++++++++"

        print "thisList = [3.4 ,2.7 ,7.7 ,1.2]"
        thisList = [3.4 ,2.7 ,7.7 ,1.2]

        print "minimum(thisList)"
        minimumValue = self.minimum(thisList)

        print "Minimum Value = " + str(minimumValue)


if __name__ == '__main__':

    MinValue().tests()
