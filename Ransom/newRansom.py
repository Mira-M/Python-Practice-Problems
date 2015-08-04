#!/usr/bin/env python
#title           :  newRansom.py
#description     :  This will create a header for a python script.
#author          :  Mira Mollar
#date            :  August 4, 2015
#version         :  1.1
#usage           :  python newRansom.py newRansom.txt newMagazine.txt - Success Case
#                :  python newRansom.py newRansom.txt magazine.txt - Fail Case 
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

    if len(ransom) > len(magazine):
        print "Sorry, ransom note can not be created from this magazine."
        sys.exit(0)

    ransomWords = {}

    for word in ransom:
        if word not in ransomWords:
            ransomWords[word.lower()] = 0
        else:
            ransomWords[word.lower()] = ransomWords.get(word) + 1

    for word in magazine:
        if word in ransomWords:
            check = ransomWords.get(word)
            print "check = " + str(check)
            print "word = " + str(word)

            check -= 1
            if check == -1:
                del ransomWords[word]
            else:
                ransomWords[word] = check

    if len(ransomWords) == 0:
        print "Congratulations! your ransom note can be created from this magazine!"
        sys.exit(0)

    print "Sorry, ransom note can not be created from this magazine."
    sys.exit(0)

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
