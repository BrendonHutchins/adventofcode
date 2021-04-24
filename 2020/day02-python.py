# ==============================
# Name: --- Day 2: Password Philosophy ---
# Author: Brendon Hutchins
# Date: 02/12/20
# Version: 1.0
# ==============================

# ==============================
# Comments: 
# 
# Part A
# For example, 1-3 a means that the password must contain a at least 1 [char] a time and at most 3 times.
# How many passwords are valid according to their policies?
# 
# Part B
# Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. 
# (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. 
# Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
# ==============================

# Imports
import re

# Globals
importedData = []
matches = 0
matchesB = 0
i = 0
j = 0
chars = 0 # count of seachValue chars found.

pattern = "-(.*?)\ "
patternMinPassword = "(.*?)\-"

# Import file and extract contents
# inputFile = open('./input/input_simple02.txt', 'r')
inputFile = open('./input/input02.txt', 'r')
importedData = inputFile.readlines()

# Part A
while i < len(importedData):
    splitString = importedData[i].split(" ", 2) # Split input entry into parts - ['1-3', 'a:', 'abcde\n']
    #minPasswordCharValue = str(importedData[i].split("-", 1))[2] # only collects the first digit
    #maxPasswordCharValue = str(importedData[i].split("-", 1))
    passwordSearchValue = splitString[1] # spit search letter, eg. a, b, c
    password = splitString[2] # set password as the third element 
    passwordSearchValue = passwordSearchValue[:1] # remove colon char 

    s = importedData[i] 
    minPasswordCharValue2 = re.search(patternMinPassword, s).group(1)

    try:
        maxPasswordCharValue = re.search(pattern, s).group(1)
    except:
        substring = None
        print("ERROR: Unable to search for max value")


   # Test Output.
    print("TEST OUTPUT: ", maxPasswordCharValue)

    # Part B
    #==========================
    # if password[int(minPasswordCharValue2)] == passwordSearchValue ^ password[int(maxPasswordCharValue)] == passwordSearchValue == True:
    #     print("GG")

    testPassword = "abc"
    #testValueB = 999897
    testValueB = 979899
    convertedToAssciValue = ""

    for char in testPassword:
        convertedToAssciValue += str(ord(char))
    #print(convertedToAssciValue)
    convertedToAssciValue = int(convertedToAssciValue)
    #testPassword = int(testPassword)
    #print(convertedToAssciValue ^ testValueB)
    if convertedToAssciValue ^ testValueB == 0:
        print("Eval FALSE: ")

#===============================
    for value in password:
        if value == passwordSearchValue:
            chars += 1
        j += 1
    #print("We found the following: ", passwordSearchValue, "Count: ", chars)

# testing that correct values are assigned to min and max
    #print("min password value: ", minPasswordCharValue2)
    # print("max password value: ", maxPasswordCharValue)

    if chars >= int(minPasswordCharValue2) and chars <= int(maxPasswordCharValue):
        #print("min: ", minPasswordCharValue2, "max: ", maxPasswordCharValue, "chars: ", chars, "search value: ", passwordSearchValue)
        matches += 1
    chars = 0
    # minPasswordCharValue = 0
    # maxPasswordCharValue = 0
    i += 1
print("Matches A: ", matches)
print("Matches B: ", matchesB)
#s.split(" ", 1)
#print(importedData[1])

# Testing

