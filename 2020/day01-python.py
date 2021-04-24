# ==============================
# Name: --- Day 1: Report Repair ---
# Author: Brendon Hutchins
# Date: 01/12/20
# Version: 1.0
# ==============================

# ==============================
# Comments: 
# Part A
# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
# 
# Part B
# They offer you a second one if you can find three numbers in your expense report that meet the same criteria.
# In your expense report, what is the product of the three entries that sum to 2020?
#
# ==============================

# Imports

# Globals
importedData = []

# Import file and extract contents
#inputFile = open('./input/input_simple01.txt', 'r')
inputFile = open('./input/input01.txt', 'r')
importedData = inputFile.readlines()

# Part A
def parta():
    i = 0
    while i < len(importedData):
        for j in range(i, len(importedData)):
            if int(importedData[i]) + int(importedData[j]) == 2020:
                print(int(importedData[i]) * int(importedData[j]))
        i += 1

# Part B
def partb():
    i = 0
    while i < len(importedData):
        for j in range(i, len(importedData)):
            for k in range(i, len(importedData)):
                #print("Location information: ", i, " ", j, " ", k):
                if int(importedData[i]) + int(importedData[j]) + int(importedData[k]) == 2020:
                    #print("Sum has been found: ", i,j,k)
                    #print((importedData[i], " ", importedData[j], " ", importedData[k]))
                    print(int(float(importedData[i])) * int(float(importedData[j])) * int(float(importedData[k])))
        i += 1

# Testing

print("part a")
parta()
print("part b")
partb()