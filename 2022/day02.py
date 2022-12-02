# ==============================
# Name: AoC Day 02
# Author: Brendon Hutchins
# Date: 02/12/22
# Version: 1.0
# ==============================

# ==============================
# Comments:
# Part A
# Play Rock, Paper Scissors. Input data defines two columns {opponent action, player action}.
# Points are awarded for a win, draw and played action. Multiple rounds are played.
# Highest cumulative sum of round scores wins.
# 3 defined states that define one of 3 possible sub-states. eg: Rock => {Scissor (win), Paper (loss), Rock (draw)}
#
# Part B
# Now input column two defines the outcome of the round.
# We need to check which sub-state has been defined, and add round points for the correct action that matches the defined outcome and outcome.
#  ==============================

# Imports
import argparse
import sys

# Globals
importedData = []
count = 0
roundTotal = 0
sumTotals = 0
currentMove = []

drawCompliment = {
    'A': 'X', # match rock
    'B': 'Y', # match paper
    'C': 'Z' # match scissor
}

# first col win check
winDictionary = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

parser = argparse.ArgumentParser(description='Parse User Input')
availableOption = ["A", "B", "T"]  # Used for any sub-options available to argument.
parser.add_argument('-A', action='store_true', help="Run Test A")
parser.add_argument('-B', action='store_true', help="Run Test B")
parser.add_argument('-T', action='store_true', help='Run Test Data')
args = parser.parse_args()

# import data from file
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
        while count < len(importedData):
            for idx in importedData[count]:  # grab first entry pair
                if idx != ' ' and idx != '\n':
                    currentMove.append(idx)
            extractedPlayerValue = currentMove[1]
            if winDictionary[currentMove[0]] == extractedPlayerValue:  # opp wins
                # roundTotal += 0
                if currentMove[1] == "X":
                    roundTotal += 1
                if currentMove[1] == "Y":
                    roundTotal += 2
                if currentMove[1] == "Z":
                    roundTotal += 3
            elif currentMove[0] == "A" and currentMove[1] == "X" or currentMove[0] == "B" and currentMove[1] == "Y" or \
                    currentMove[0] == "C" and currentMove[1] == "Z":  # Draw. Yes I hate it too
                roundTotal += 3
                if currentMove[1] == "X":
                    roundTotal += 1
                if currentMove[1] == "Y":
                    roundTotal += 2
                if currentMove[1] == "Z":
                    roundTotal += 3
            else:  # Player wins
                if currentMove[1] == "X":
                    roundTotal += 1
                if currentMove[1] == "Y":
                    roundTotal += 2
                if currentMove[1] == "Z":
                    roundTotal += 3
                roundTotal += 6

            sumTotals += roundTotal
            roundTotal = 0
            currentMove.clear()
            count += 1
        print("Sum Total: ", sumTotals)
if args.B:
    print("Running section B\n")
    while count < len(importedData):
        for idx in importedData[count]:  # grab first entry pair
            if idx != ' ' and idx != '\n':
                currentMove.append(idx)
        extractedPlay = currentMove[1]
        extractedOppValue = currentMove[0]

        # check if we win, lose or draw
        if extractedPlay == 'X':  # we lose
            if extractedOppValue == "A":
                roundTotal += 3 # opp rock, you scissor =3
            if extractedOppValue == "B":
                roundTotal += 1 # opp paper, you rock =1
            if extractedOppValue == "C":
                roundTotal += 2 # opp scissor, you paper =2

        if extractedPlay == 'Y':  # we draw
            roundTotal += 3
            if extractedOppValue == "A":
                roundTotal += 1  # opp rock, you rock =1
            if extractedOppValue == "B":
                roundTotal += 2  # opp paper, you paper =2
            if extractedOppValue == "C":
                roundTotal += 3  # opp scissor, you scissor =3

        if extractedPlay == 'Z':  # we win
            roundTotal += 6
            if extractedOppValue == "A":
                roundTotal += 2  # opp rock, you paper =2
            if extractedOppValue == "B":
                roundTotal += 3  # opp paper, you scissor =3
            if extractedOppValue == "C":
                roundTotal += 1  # opp scissor, you rock =1
        sumTotals += roundTotal
        roundTotal = 0
        currentMove.clear()
        count += 1
    print("Sum Total", sumTotals)

if args.T:
    print("Running Test data simple_input.txt\n")

# Print Output
if not importedData:
    print("Error: No data is currently loaded")