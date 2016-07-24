# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
A1.pdf answer
Tingyu Yang(Claire)
"""

#Question 1
def sum(values):
    result = 0
    for v in values:
        result = result + v
    return result
    
def product(values):
    result =1
    for v in values:
        result = result * v
    return result
    
#Question 2
def longest(words):
    result = words[0]
    for w in words:
        if len(w) > len(result):
            result = w
        return result
        
def shortest(words):
    result = words[0]
    for w in words:
        if len(w) <len(result):
            result = w
        return result
        
#Question 3
def average(values):    
    result = 0
    count = len(values)
    for v in values:
        result =result + v
    result = result/count
    return result
        
#Question 4
import random
def dice():
    counter=0
    diceCount={2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
    while (counter<100):
        random1 = random.randint(1,6)
        random2 = random.randint(1,6)
        randsum = random1 + random2
        diceCount[randsum] = diceCount[randsum]+1
        print (randsum)       
        counter = counter+1
    countSum=2
    while (countSum<3):
        print("{}:{}".format(countSum, diceCount[countSum])
        countSum+=1

        
#Question 5
def five():
    print("Think of a number between 1 and 1000.")
    min = 1
    max = 1000
    while (min < max):
        guess = (min + max) // 2
        answer = input("Is it more than {} (y/n)? ".format(guess))
        answer= answer.lower()
        test = answer.startswith("y")
        if answer == "y" or test==True:
            min = guess + 1
        else:
            max = guess
# At this point min and max must be the same
    print("Your number is {}.".format(min))
    
    
