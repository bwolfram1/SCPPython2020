# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 17:05:24 2020

@author: brand
"""

import sys
import random
def makeYourChoice():
    print("Press R for Rock")
    print("Press P for Paper")
    print("Press S for Scissors")
    print("Press Q for Quit!")
    uChoice = input("What do you want to choose?").lower()
    if uChoice == "r":
        return "Rock"
    if uChoice == "p":
        return "Paper"
    if uChoice == "s":
        return "Scissors"
    if uChoice == "q":
        sys.exit(0)
    else: 
        makeYourChoice()
def cRandom():
    options = ["Rock","Paper","Scissors"]
    randomChoice = random.randint(0,2)
    return options[randomChoice]
def comparison(hChoice, cChoice):
    if hChoice == cChoice:
        return "Draw"
    if hChoice == "Rock" and cChoice == "Paper":
        return "Computer Wins!"
    if hChoice == "Paper" and cChoice == "Scissors":
        return "Computer Wins!"
    if hChoice == "Scissors" and cChoice == "Rock":
        return "Computer Wins!"
    else:
        return "Human wins!"
while True:
    
    hChoice = makeYourChoice()
    cChoice = cRandom()
    print("You chose: ", hChoice)
    print("The computer chose: ", cChoice)
    result = comparison(hChoice, cChoice)
    if result == "Draw":
        print("It was a draw")
    elif result == "Computer Wins!":
        print("You lost!")
    else: 
        print("You won!")
    print("")