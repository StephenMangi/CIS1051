## Stephen Mangiaracina Exam 3

def evenWords(stringList):
    count = 0
    for word in stringList:
        if len(word) % 2 == 0:
            count += 1
    return count

## Problem # 2

# sumOfLargests([[1,2,3], [-1,-2,-3], [1000]]) -> 1002
# sumOfLargests([[5,1,-2,3], [4,3,-7], [1,2]]) -> 11
def sumOfLargests(listOfLists):
    largestNums = []
    for i in listOfLists:
        largestNums.append(max(i))
    return sum(largestNums)

# Problem 3

'''
Food,10/14/2022,5.59
Virtual Instrument,9/15/2022,29.00
Food,11/14/2021,$13.21
Travel,04/06/2055,50.00
Gas,02/16/2021,49.57
Bill,9/17/2022,82.73
'''

def notFoodSum(Purchases):
    data = open(Purchases,'r')
    for line in data:
        sum = 0
        fields = line.split(',')
        if fields(0) != "Food":
            sum +=1
        return sum
    


# Problem 4

#mostCommonWord("this is the story of the boy in the red hat") -> "the"
#mostCommonWord("buffalo buffalo buffalo buffalo buffalo buffalo buffalo buffalo is a grammatically correct sentence") -> "buffalo"
#mostCommonWord("did you ever hear the tragedy of darth plagueis the wise") -> "the"
def mostCommonWord(text):
	d = { }
	for word in text:
		if word not in d:
			d[word] = 1
		else:
			d[word] += 1
	mostComWord = text[0]
	for letter in d:
		if d[word] > d[mostComWord]:
			mostComWord = word
	return mostComWord
print(mostCommonWord)


# Problem 5

import random
def flip( ):
	return random.choice(['H','T'])

def coinFlips(seq1)
    history = flip()+flip()+flip()+flip()+flip()+flip()+flip()+flip()+flip()+flip()
    if history != seq1
        history += flip()
    return history[-3] == seq1

def simCoinFlips():
    wins = 0
    trials = 100000
    for i in range(trials):
        if coinFlips('HHHHHTTTTT'):
            wins += 1
        print(wins/trials)

simCoinFlips()