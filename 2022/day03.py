# ==============================
# Name: AoC Day 03
# Author: Brendon Hutchins
# Date: 03/12/22
# Version: 1.0
# ==============================

# ==============================
# Comments:
# Part A
# Find the common character between the first half of the string and the second half of the string.
#
# Part B
# Find the common character between each group of three lines.
#
#  ==============================

# Imports
import argparse
import sys

# Globals
importedData = []

prioritySum = 0
secondSum = 0
dupeIndex = []
storage = []
count = 0
elfGroup = 3

parser = argparse.ArgumentParser(description='Parse User Input')
availableOption = ["A", "B", "T"]  # Used for any sub-options available to argument.
parser.add_argument('-A', action='store_true', help="Run Test A")
parser.add_argument('-B', action='store_true', help="Run Test B")
parser.add_argument('-T', action='store_true', help='Run Test Data')
args = parser.parse_args()

# import data from file
inputFilePath = './input/input03.txt'
#inputFilePath = './input/input_simple03.txt'

try:
    inputFile = open(inputFilePath, 'r')
except IOError:
    print("The specified file could not be loaded")
    sys.exit(1)

importedData = inputFile.readlines()
if args.A:
    print("Running section A\n")
    for idx in importedData:  # grab full line
        tempLength = len(idx)
        firstHalf, secondHalf = slice(0, tempLength//2), slice(tempLength//2, tempLength) # extract length indices
        for firstHalfChar in idx[firstHalf]:
            for secondHalfChar in idx[secondHalf]:
                if firstHalfChar == secondHalfChar and firstHalfChar not in dupeIndex:
                    dupeIndex.append(firstHalfChar)
                    break
        for entry in dupeIndex:
            if entry.isupper():
                prioritySum += ord(entry) - 38  # setting off-set for the provided upper value range 27 <-> 52
            elif entry.islower():
                prioritySum += ord(entry) - 96
        dupeIndex.clear()
print("Sum Total: ", prioritySum)

if args.B:
    print("Running section B\n")
    for idx in importedData:  # grab full line
        if count < elfGroup:
            storage.append(idx)
        if len(storage) == elfGroup:
            for firstStorageChar in storage[0]:
                if firstStorageChar in storage[0] and firstStorageChar in storage[1] and firstStorageChar in storage[2]:
                    break
            if firstStorageChar.isupper():
                secondSum += ord(firstStorageChar) - 38
            if firstStorageChar.islower():
                secondSum += ord(firstStorageChar) - 96
            storage.clear()
print("Sum Total: ", secondSum)

if args.T:
    print("Running Test data simple_input.txt\n")

# Print Output
if not importedData:
    print("Error: No data is currently loaded")