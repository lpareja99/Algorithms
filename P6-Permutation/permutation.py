'''
Program 6 Permutation
@auhors: Laura Pareja & Isaac Schmidt 
Date: 10/9/2019
Date Last Modified: 10/9/2019
Description: 
'''
import math 

DEBUG = False

def LexicographicPermute(n):

    listNumber = []

    for e in range(1, n+1):
        listNumber.append(e)


	#initiate list to hold all permutations
    listPermutation = []
    done = False
    totalPermutations = 0
    while(done == False):
    
    #add new permutation to list of already existing permutations
        for i in range(n-1):
            if(listNumber not in listPermutation):
                listPermutation.append(listNumber)
                totalPermutations = totalPermutations+1
      
    #find i index
    i = n-2
    while(listNumber[i]>listNumber[i+1]):
      	i = i-1
  
    #find j index
    j = n-1
    while(listNumber[i]>listNumber[j]):
      	j = j-1

    
    #swap position of i and j
    temporal = listNumber[i]
    listNumber[i] = listNumber[j]
    listNumber[j] = temporal

    #reverse from i+1 to n inclusive
    subListA = listNumber[:i+1]
    subListB = listNumber[i+1:]
    subListB.reverse()
    listNumber = subListA + subListB
    done = checkCondition(listNumber,n)


    print (listPermutation)
    print (len(listPermutation))

# fuction to check if we arrived to the last permutation (Ex:4,3,2,1)
def checkCondition(lastPermute, numOfNumbers):
    for x in range(0,numOfNumbers-1):
        if lastPermute[x] < lastPermute[x+1]:
            return False
    return True

def reverse(li):
  	return li[::-1]

LexicographicPermute(4)