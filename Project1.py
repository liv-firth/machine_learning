# -*- coding: utf-8 -*-
############################ PROJECT 1 #################################

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: Liberty Bell Slot Machine
# Olivia Firth 
# Last Modified: September 14th, 2019
# ---------------------------------------
# Simulate a modified Liberty Bell Slot Machine.
# ---------------------------------------

import random

# Constants that represent the result of spinning a reel
DIAMOND = 1     
HEART = 2
SPADE = 3
HORSESHOE = 4
LIBERTY_BELL = 5

# ---------------------------------------
# spin_payout
# ---------------------------------------
# reel_1: the symbol on the first reel, an integer constant
# reel_2: the symbol on the second reel, an integer constant
# reel_3: the symbol on the third reel, an integer constant
# ---------------------------------------
# Returns an integer, the payout of the spin
# ---------------------------------------

""" The missing spin_payout function goes here ... """
#Calculating Pay Out from Individual Spin.
def spin_payout(reel_1, reel_2, reel_3):
        payout = 0
        #Cases with three of the same symbol
        if reel_1 == reel_2 == reel_3:
                if reel_1 == DIAMOND:
                        payout = 30
                elif reel_1 == HEART:
                        payout = 40
                elif reel_1 == SPADE:
                        payout = 20
                elif reel_1 == HORSESHOE:
                        payout = 10
                elif  reel_1 == LIBERTY_BELL:
                        payout = 50
        #Cases with two horshoes 
        elif  reel_1 == reel_2 == HORSESHOE or reel_1 == reel_3 == HORSESHOE or reel_2 ==  reel_3 == HORSESHOE:
                        payout = 5
        else: payout = 0
        
        return(payout);

	
        
# ---------------------------------------
# convert
# ---------------------------------------
# reel: the symbol on a reel, an integer constant
# ---------------------------------------
# Returns a string, the printing value of integer
# ---------------------------------------

def convert(reel):
    if reel == DIAMOND:
        return "diamond"
    elif reel == HEART:
        return "heart"
    elif reel == SPADE:
        return "spade"
    elif reel == HORSESHOE:
        return "horseshoe"
    elif reel == LIBERTY_BELL:
        return "bell"
    else:
        return "error!"

# ---------------------------------------
# test_known_spin
# ---------------------------------------
# reel_1: the symbol on the first reel, an integer constant
# reel_2: the symbol on the second reel, an integer constant
# reel_3: the symbol on the third reel, an integer constant
# ---------------------------------------
# Display a message that shows the spin and its payout
# ---------------------------------------

def test_known_spin(reel_1, reel_2, reel_3):
    message = "{:10}".format(convert(reel_1))
    message += "{:10}".format(convert(reel_2))
    message += "{:10}".format(convert(reel_3))
    message += "{:-6d}".format(spin_payout(reel_1, reel_2, reel_3))
    print(message)

# ---------------------------------------
# test_known_spins
# ---------------------------------------
# For testing purposes, evaluate a variety of known spins
# ---------------------------------------

def test_known_spins():
    print("{:10}{:10}{:10}{}".format("REEL 1", "REEL 2", "REEL 3", "PAYOUT"))
    print("{:10}{:10}{:10}{}".format("------", "------", "------", "------"))
    test_known_spin(LIBERTY_BELL, LIBERTY_BELL, LIBERTY_BELL)
    test_known_spin(HEART, HEART, HEART)
    test_known_spin(DIAMOND, DIAMOND, DIAMOND)
    test_known_spin(SPADE, SPADE, SPADE)
    test_known_spin(HORSESHOE, HORSESHOE, HORSESHOE)
    test_known_spin(HORSESHOE, HORSESHOE, HEART)
    test_known_spin(HORSESHOE, DIAMOND, HORSESHOE)
    test_known_spin(SPADE, HORSESHOE, HORSESHOE)
    test_known_spin(HEART, HEART, HORSESHOE)
    test_known_spin(LIBERTY_BELL, DIAMOND, SPADE)

# ---------------------------------------
# simulate
# ---------------------------------------
# how_many: the number of spins to take, an integer
# ---------------------------------------
# Simulate the Liberty Bell Slot Machine being played
# how_many times.  Calculate and print the expected winnings.
# ---------------------------------------

""" The missing simulate function goes here ... """
def simulate(how_many):
        
        counter_payout = 0
        
        for x in  range(how_many):
            #Generate random integer between 1 and 5 for each reel
            reel_1 = random.randint(1,5)
            reel_2 = random.randint(1,5)
            reel_3 = random.randint(1,5)
            #Calling spin_payout function and converting from cents to dollars 
            pay_per_spin = 0.01*spin_payout(reel_1, reel_2, reel_3)
            #Spin Pay Out Counter
            counter_payout = counter_payout + pay_per_spin
        #Calculating average pay out per spin 
        average_spin = counter_payout/how_many
        #Calculating the average pay out when you spend a dollar which allows you to spin 20 times
        averagedollar_spin = average_spin*20
        print("If you spin the machine" ,(how_many), "times, you are expected to win an average of" ,round(average_spin, 5), "dollars per spin.")
        print("If you spend a dollar to spin the machine twenty times, you are expected to win", round(averagedollar_spin, 5), " dollars.")

# ---------------------------------------
# main - controls the main flow of logic
# ---------------------------------------

def main():
    print("Program 1: Liberty Bell Slot Machine Simulation\n")
    print("--> Part 1: Testing Known Spins\n")
    test_known_spins()
    print("\n--> Part 2: Simulating 500,000 Spins\n")
    simulate(500000)
          
# ---------------------------------------

main()
