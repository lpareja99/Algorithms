'''
Program 6 Permutation
@auhors: Laura Pareja & Isaac Schmidt 
Date: 10/9/2019
Date Last Modified: 10/10/2019
'''

'''
------> PART 2:
'''

# permunte(): main function to permute trough n numbers
# -Inputs:
#   n: number of numbers to permute
# -Outputs: 
#   listPermutation: list with all posible permutation
def permute(n):

  #create list with original number from 0 to n
  listNumber= []
  for e in range(1,n + 1):
    listNumber.append(e)

  #initiate list to hold all permutations
  listPermutation = []
  
  #add new permutation to list of already existing permutations
  listPermutation.append(listNumber[:])

  #done condition to check if we have to continue
  done = checkCondition(listNumber,n)
  #stop when the whole array is traversed
  while(done == False):

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

    #add new permutation to list of already existing permutations 
    listPermutation.append(listNumber[:])

  #returns list of Permutations
  return listPermutation

# checkCondition():
# fuction to check if we arrived to the last permutation (Ex:4,3,2,1)
# -Inputs:
#   -lasrPermute: array with elements to check
#   -numOfNumbers: how many elements there are in the array
# -Output:
#   -boolean: true or false
def checkCondition(lastPermute, numOfNumbers):
  for x in range(0,numOfNumbers-1):
    if lastPermute[x] < lastPermute[x+1]:
      return False
  return True

#tests for single number input
def test():
  print(permute(1))
  print(permute(2))
  print(permute(3))
  print(permute(4))
  print(permute(5))


test()
#-------------------------------------------------------------------
'''
-----> PART 3:
'''

# permunte(): main function to permute trough a given array of elements
# -Inputs:
#   listNumber: list with the elements to permute
# -Outputs: 
#   listPermutation: list with all posible permutation
def permuteList(listNumber):

  #order the array
  listNumber.sort()

  #lenght of the array
  n = len(listNumber)

  #initiate list to hold all permutations
  listPermutation = [] 

  string = ""
  for i in range(n):
    string = string + str(listNumber[i])
  listPermutation.append(string)

  #done condition to check if we have to continue
  done = False
  #stop when the whole array is traversed
  while(done == False):
    done = checkConditionList(listNumber,n)
    
    #find i index
    i = n-2
    while(listNumber[i]>=listNumber[i+1]):
      i = i-1
  
    #find j index
    j = n-1
    while(listNumber[i]>=listNumber[j]):
      j = j-1

    
    #swap position of i and j
    temporal = listNumber[i]
    listNumber[i] = listNumber[j]
    listNumber[j] = temporal

    #reverse from i+1 to n inclusive
    subListA = listNumber[:i+1]
    subListB = listNumber[i+1:]
    subListB.reverse()
    listNumber= subListA + subListB
    done = checkCondition(listNumber,n)


    #add new permutation to list of already existing permutations
    string = ""
    for i in range(n):
      string = string + str(listNumber[i])
    listPermutation.append(string)

  #returns list of Permutations
  return listPermutation


# fuction to check if we arrived to the last permutation (Ex:4,3,2,1)
# -Inputs:
#   -lasrPermute: array with elements to check
#   -numOfNumbers: how many elements there are in the array
# -Output:
#   -boolean: true or false
def checkConditionList(lastPermute, numOfNumbers):
  for x in range(0,numOfNumbers-1):
    if lastPermute[x] < lastPermute[x+1]:
      return False
  return True


#given testCase Function
def testCase(testNumber, inputList,expectedResult):
  actualResult = permuteList(inputList)
  if actualResult == expectedResult: print('Test  ',testNumber,' passed.')
  else: print('Test  ',testNumber,' failed.')

#test function to call tests
def test():
  #given tests
  testCase(1,['a','a','b','b'], ['aabb','abab','abba','baab','baba','bbaa'])

  #new Tests
  testCase(2, ['a','b','r','x'], ['abrx', 'abxr','arbx','arxb', 'axbr','axrb', 'barx','baxr', 'brax', 'brxa', 'bxar', 'bxra', 'rabx', 'raxb', 'rbax', 'rbxa', 'rxab', 'rxba', 'xabr', 'xarb', 'xbar', 'xbra', 'xrab', 'xrba'])
  testCase(3, ['a', 'a', 'b'], ['aab', 'aba', 'baa'])
  testCase(4, [1, 2, 3], ['123', '132', '213', '231', '312', '321'])
  testCase(5,['a','b','b','c'],['abbc','abcb','acbb','babc','bacb','bbac','bbca','bcab','bcba','cabb','cbab','cbba'])
  testCase(6,['a','a','a','b'],['aaab','aaba','abaa','baaa'])
  testCase(7,['b','a'],['ab','ba'])
  testCase(8,['x','a','b','r'], ['abrx', 'abxr','arbx','arxb', 'axbr','axrb', 'barx','baxr', 'brax', 'brxa', 'bxar', 'bxra', 'rabx', 'raxb', 'rbax', 'rbxa', 'rxab', 'rxba', 'xabr', 'xarb', 'xbar', 'xbra', 'xrab', 'xrba'])
  
test()