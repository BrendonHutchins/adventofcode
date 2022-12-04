# ==============================
# Name: AoC Day 04
# Author: Brendon Hutchins
# Date: 04/12/22
# Version: 1.0
# ==============================

# ==============================
# Comments:
# Part A
# Count all instances of value1 range eg: [200-500] being fully contained in value2 range [300-400] and vice versa.
#
# Part B
# Count all instances of overlap [inclusive] of the provided bounded sets.
#
#  ==============================

# Imports
import argparse
import sys

# Globals
importedData = []
fullyBoundedCount = 0
partBoundsCount = 0

parser = argparse.ArgumentParser(description='Parse User Input')
availableOption = ["A", "B", "T"]  # Used for any sub-options available to argument.
parser.add_argument('-A', action='store_true', help="Run Test A")
parser.add_argument('-B', action='store_true', help="Run Test B")
parser.add_argument('-T', action='store_true', help='Run Test Data')
args = parser.parse_args()

# import data from file
inputFilePath = './input/input04.txt'
#inputFilePath = './input/input_simple04.txt'

try:
    inputFile = open(inputFilePath, 'r')
except IOError:
    print("The specified file could not be loaded")
    sys.exit(1)

importedData = inputFile.readlines()
if args.A:
    print("Running section A\n")
    for idx in importedData:
        inputStripped = idx.strip() #  remove '\n' 
        valueOne, valueTwo = inputStripped.split(',')
        valueOneStart, valueOneEnd = valueOne.split('-')
        valueTwoStart, valueTwoEnd = valueTwo.split('-')
        if int(valueOneStart) >= int(valueTwoStart) and int(valueOneEnd) <= int(valueTwoEnd) or int(valueTwoStart) >= int(valueOneStart) and int(valueTwoEnd) <= int(valueOneEnd):
            fullyBoundedCount += 1
print("Total Sum : ", fullyBoundedCount)

if args.B:
    print("Running section B\n")
    for idx in importedData:
        inputStripped = idx.strip() #  remove '\n'
        valueOne, valueTwo = inputStripped.split(',')
        valueOneStart, valueOneEnd = valueOne.split('-')
        valueTwoStart, valueTwoEnd = valueTwo.split('-')
        if int(valueTwoStart) <= int(valueOneEnd) <= int(valueTwoEnd) or int(valueOneStart) <= int(valueTwoStart) <= int(valueOneEnd) or int(valueOneStart) <= int(valueTwoEnd) <= int(valueOneEnd):
            partBoundsCount += 1
print("Total Sum: ", partBoundsCount)

if args.T:
    print("Running Test data simple_input.txt\n")

#  Print Output
if not importedData:
    print("Error: No data is currently loaded")