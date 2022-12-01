# ==============================
# Name: AoC Day 01
# Author: Brendon Hutchins
# Date: 01/12/22
# Version: 1.0
# ==============================

# ==============================
# Comments:
# Part A
# Sum the groups of provided numbers delimited by '\n'. Print the largest value.
#
# Part B
# Rank order and print the total of the largest 3 groups.
#
#  ==============================

# Imports
import argparse
import sys

# Globals
importedData = []
sumCount = 0
storedTotal = []
importedDataPos = 1 # used to track our idx through the list.

parser = argparse.ArgumentParser(description='Parse User Input')
availableOption = ["A", "B", "T"]  # Used for any sub-options available to argument.
parser.add_argument('-A', action='store_true', help="Run Test A")
parser.add_argument('-B', action='store_true', help="Run Test B")
parser.add_argument('-T', action='store_true', help='Run Test Data')
args = parser.parse_args()

# import data from file
inputFilePath = './input/input01.txt'
#inputFilePath = './input/input_simple01.txt'
try:
    inputFile = open(inputFilePath, 'r')
except IOError:
    print("The specified file could not be loaded")
    sys.exit(1)

importedData = inputFile.readlines()

if args.A:
    print("Running section A\n")
    for idx in importedData:
        if idx != '\n':
            sumCount += int(idx)
            if importedDataPos == len(importedData): # Case where this is the last item in the list.
                storedTotal.append(sumCount)
        else:
            storedTotal.append(sumCount)
            sumCount = 0
        importedDataPos += 1

    if storedTotal:
        print(max(storedTotal))

if args.B:
    print("Running section B\n")
    for idx in importedData:
        if idx != '\n':
            sumCount += int(idx)
            if importedDataPos == len(importedData): # Case where this is the last item in the list.
                storedTotal.append(sumCount)
        else:
            storedTotal.append(sumCount)
            sumCount = 0
        importedDataPos += 1
    if storedTotal:
        storedTotal.sort(reverse=True)
        print(storedTotal[0] + storedTotal[1] + storedTotal[2])

if args.T:
    print("Running Test data simple_input.txt\n")

# Print Output
if not importedData:
    print("Error: No data is currently loaded")
