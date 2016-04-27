## Njeri Cooper
## 4/20/16
##Dice Program


from random import random

def rollDice():
    for i in range(0, 7):
        roll = int(random.randint(1,6))
        rollCount[roll - 1] += 1
    return rollCount

def percentage(part, whole):
    return 100*float(part)/float(whole)

def displayResult(rollCount, numTimes):
    actualPercent = []
    print ('Dice Total  Number Occurances  Percentage  Expected Percent')
    for i in range(1, 7):
        print (rollCount)
    return actualPercent    
        
numTimes = int(input('Enter number of dice rolls: '))
rollCount = []*6 
for i in range (numTimes):
    die1 = rollDice()
    die2 = rollDice()
    rollCount[die1+die2] += 1
displayResult(rollCount, numTimes)
