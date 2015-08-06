#!/usr/bin/env python
#title           :  reversedll.py
#description     :  This will create a header for a python script.
#author          :  Mira Mollar
#date            :  August 5, 2015
#version         :  1.0
#usage           :  python reversedll.py
#notes           :  This script is a practice problem for learning python :)
#                   This file will implement a reversed linked list in Python
#python_version  :  2.7

class Reverse():

    def __init__(self):
        self.myList = []
        self.head = 0
        self.index = 2

    def reversed(self, item):
        self.myList = item

        self.myList.append(self.myList[self.head])
        print "My List = " + str(self.myList)

        print "len(myList) = " + str(len(self.myList))

        for i in range(1, 3):
            self.myList[0] = self.myList[len(self.myList) - self.index]
            self.myList[len(self.myList) - self.index] = self.myList[i + 1]
            print "i = " + str(i)
            self.index += 1

        print self.myList

        return self.myList

    def tests(self):
        print "+++++++++++ Test 1: Example Case from Brainstorming ++++++++++"

        thisList = ['One', 'Two', 'Three', 'Four']

        print "reversed(thisList)"
        newList = self.reversed(thisList)
        print "newList = " + str(newList)

if __name__ == '__main__':

    Reverse().tests()
