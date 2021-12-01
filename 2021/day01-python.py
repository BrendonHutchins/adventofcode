# ==============================
# Name: AoC Day 01
# Author: Brendon Hutchins
# Date: 01/12/21
# Version: 1.0
# ==============================

# ==============================
# Comments: 
# Part A
# Find all instances of a number increase between each pair of numbers going forward through the array.
# 
# Part B
# Sliding window in increments of 3. Sum the current window and compare to the sum of the previous. If value has increased add to running increment total.
# 
#  ==============================

# Imports
import argparse
import sys

# Globals
importedData = []
i = -1
count = 0
currentTotal = 0
previousTotal = 0
windowSize = 3
increaseDetected = 0

parser = argparse.ArgumentParser(description='Parse User Input')
availableOption = ["A", "B", "T"] # Used for any sub-options available to argument.
parser.add_argument('-A', action='store_true', help="Run Test A")
parser.add_argument('-B', action='store_true', help="Run Test B")
parser.add_argument('-T', action='store_true', help='Run Test Data')
args = parser.parse_args()

#import data from file
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
    while i < len(importedData):
        if(i == 0):
            pass
        if(importedData[i] > importedData[(i-1)]):
            count += 1
        i += 1
print(count)

if args.B:
    print("Running section B\n")
    for i in range(len(importedData) - windowSize):
        extractedSlice = importedData[i:i + windowSize]
        for j in extractedSlice:
            currentTotal += int(j)
       
        if(currentTotal > previousTotal):
            increaseDetected +=1
        previousTotal = currentTotal
        currentTotal = 0
print(increaseDetected)

if args.T:
    print("Running Test data simple_input.txt\n")

# Print Output
if not importedData:
    print("Error: No data is currently loaded")
