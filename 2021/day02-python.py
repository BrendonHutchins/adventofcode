# ==============================
# Name: AoC Day 02
# Author: Brendon Hutchins
# Date: 02/12/21
# Version: 1.0
# ==============================

# ==============================
# Comments: 
# Part A
#  Track two axis. (1) Horizontal position mapped to 'forward'. (2) Depth position which is calculated from the values of "Up" and "Down"/ submit the product of these two axis.
# 
# Part B
#  Track value "aim". increasing depth by the 'down' || 'up' command will have a corresponding value impact on the value 'aim'.
#  'Forward' command will affect the value on the x axis &&  adjust the depth value => aim * x = depth  
# 
#  ==============================

#Imports
import argparse
import sys

# Globals
importedData = []
idx = 0
depth = 0
forward = 0
aim = 0

parser = argparse.ArgumentParser(description='Parse User Input')
availableOption = ["A", "B", "T"] # Used for any sub-options available to argument.
parser.add_argument('-A', action='store_true', help="Run Test A")
parser.add_argument('-B', action='store_true', help="Run Test B")
parser.add_argument('-T', action='store_true', help='Run Test Data')
args = parser.parse_args()

#import data from file
inputFilePath = './input/input02.txt' 
#inputFilePath = './input/input_simple02.txt' 
try:
    inputFile = open(inputFilePath, 'r')
except IOError:
    print("The specified file could not be loaded")
    sys.exit(1)

importedData = inputFile.readlines()

if args.A:
    print("Running section A\n")
    while idx < len(importedData):
        extractedSlice = importedData[idx:idx+1]
        extractedCommand = extractedSlice[0].split()

        if extractedCommand[0] == "up":
            depth -= int(extractedCommand[1])
        if extractedCommand[0] == "down":
            depth += int(extractedCommand[1])
        if extractedCommand[0] == "forward":
            forward += int(extractedCommand[1])     
        idx += 1
    print(forward * depth)

if args.B:
    print("Running section B\n")

    while idx < len(importedData):
        extractedSlice = importedData[idx:idx+1]
        extractedCommand = extractedSlice[0].split()
        if extractedCommand[0] == "up":
            aim -= int(extractedCommand[1])
        if extractedCommand[0] == "down":
            aim += int(extractedCommand[1])
        if extractedCommand[0] == "forward":
            forward += int(extractedCommand[1])
            depth += aim * int(extractedCommand[1])
        idx += 1
    print(forward * depth)

if args.T:
    print("Running Test data simple_input.txt\n")

# Print Output
if not importedData:
    print("Error: No data is currently loaded")
