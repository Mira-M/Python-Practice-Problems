#!/usr/bin/env python
#title           :  stackedqueue.py
#description     :  This will create a header for a python script.
#author          :  Mira Mollar
#date            :  August 4, 2015
#version         :  1.0
#usage           :  python stackedqueue.py
#notes           :  This script is a practice problem for learning python :)
#                   This file will implement a queue using two stacks
#python_version  :  2.7

class StackedQueue():

    def __init__(self):
        self.stackOne = []
        self.stackTwo = []

    # enqueue() takes the item and adds it into StackOne
    def enqueue(self, item):
        self.stackOne.append(item)

    '''
        dequeue() removes all but the first item in StackOne and places
        it in order onto StackTwo. Then it saves the first value then
        places the items in Stack Two into Stack one in order before
        returning the first value of StackOne.
    '''
    def dequeue(self):
        if len(self.stackOne) == 0:
            return None

        while len(self.stackOne) is not 1:
            self.stackTwo.append(self.stackOne.pop())

        result = self.stackOne.pop()

        while len(self.stackTwo) is not 0:
            self.stackOne.append(self.stackTwo.pop())

        return result

    '''

    '''

    def tests(self):
        print "+++++++++++ Test 1: Example Case from Brainstorming ++++++++++"
        print "enqueue(7)"
        self.enqueue(7)
        print "enqueue(4)"
        self.enqueue(4)

        remove = self.dequeue()
        print "dequeue() = " + str(remove)

        remove = self.dequeue()
        print "dequeue() = " + str(remove)

        remove = self.dequeue()
        print "dequeue() = " + str(remove)

        print ""

        print "+++++++++++ Test 2: Negative Integer ++++++++++"
        print "enqueue(1)"
        self.enqueue(1)
        print "enqueue(2)"
        self.enqueue(2)
        print "enqueue(-4)"
        self.enqueue(-4)

        remove = self.dequeue()
        print "dequeue() = " + str(remove)

        remove = self.dequeue()
        print "dequeue() = " + str(remove)

        remove = self.dequeue()
        print "dequeue() = " + str(remove)

        print "+++++++++++ Test 3: String Types ++++++++++"
        print "enqueue('Bacon')"
        self.enqueue('Bacon')
        print "enqueue('Eggs')"
        self.enqueue('Eggs')
        print "enqueue('Sugar')"
        self.enqueue('Sugar')

        remove = self.dequeue()
        print "dequeue() = " + str(remove)

        remove = self.dequeue()
        print "dequeue() = " + str(remove)

        remove = self.dequeue()
        print "dequeue() = " + str(remove)

        remove = self.dequeue()
        print "dequeue() = " + str(remove)

        print "+++++++++++ Test 3: Larger integer Values ++++++++++"
        print "enqueue(5000000 * 5000000000)"
        self.enqueue(5000000 * 5000000000)
        print "enqueue(300000000000000 * 2402304320492309409234)"
        self.enqueue(300000000000000 * 2402304320492309409234)

        remove = self.dequeue()
        print "dequeue() = " + str(remove)

        remove = self.dequeue()
        print "dequeue() = " + str(remove)

        remove = self.dequeue()
        print "dequeue() = " + str(remove)

        remove = self.dequeue()
        print "dequeue() = " + str(remove)
if __name__ == '__main__':

    StackedQueue().tests()
