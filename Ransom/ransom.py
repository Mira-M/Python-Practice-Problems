#!/usr/bin/env python
#title           :  ransom.py
#description     :  This will create a header for a python script.
#author          :  Mira Mollar
#date            :  August 4, 2015
#version         :  1.0
#usage           :  python ransom.py ransomNote.txt magazine.txt
#notes           :  This script is a practice problem for learning python :)
#                   This file will take a txt file containing a ransom note and
#                   a txt file containing magazine content.  The script will
#                   search to see if a a ransom note can be cut from the magazine.
#python_version  :  2.6.6

import sys

'''
    This function turns the file input into an array list with each word
    saved in its own index and passes this data to the check function
'''
def parse(ransomNote, magazine):

    ransom = []
    parsedRansom = ''.join(ransomNote)
    ransomWords = parsedRansom.split()
    for word in ransomWords:
        ransom.append(word)

    parsedMagazine = ''.join(magazine)
    magazineWords = parsedMagazine.split()
    magazine = []
    for word in magazineWords:
        magazine.append(word)

    check(ransom, magazine)

'''
    This function receives the parsed ransom note and magazine text and compares
    each letter in the ransom note to each letter in the magazine.  The ransom
    note is compared to the magazine due to the assumption tha the ransom note
    is shorter than the magazine.
'''
def check(ransom, magazine):
    for item in ransom:
        test = canRansom(item, magazine)
        if test == False:
            print "Sorry, ransom note can not be created from this magazine."
            sys.exit(0)

    if test == True:
        print "Congratulations! your ransom note can be created from this magazine!"

'''
    canRansom() is a helper function to the check() function that does the comparing
    of a single word in the ransom note against all text in the magazine text.
    This function returns True if the word is found, and returns false if it isnt.
'''
def canRansom(item, magazine):
    for word in magazine:
        if item.lower() == word.lower():
            return True
    return False


if __name__ == '__main__':

    if len(sys.argv) == 3:
        ransomFile = sys.argv[1]
        magazineFile = sys.argv[2]
        f = open(ransomFile)
        ransomNote = f.readlines()
        f.close()
        f = open(magazineFile)
        magazine = f.readlines()
        f.close()

    parse(ransomNote, magazine)
