'''
Program 7 Russian Multiplication
@auhors: Laura Pareja & Isaac Schmidt 
Date: 10/13/2019
Date Last Modified: 10/14/2019
'''

'''
russianMultiply(): function to multiply two numbers using the russian multiply example from the text book.
* Inputs:
  - n & m: positive numbers 
* Outputs:
  - results: array with the final sum and total number of counts.
'''
import math

def russianMultiply(n,m):

  #calculate initial operation
  result = [];
  remainder = 0;
  counter = 0;
  
  while(n != 1):
    #if n in even
    if (n%2 == 0):
      n = math.floor(n/2);

    #if n is odd
    else:
      n = (n-1)/2;
      counter = counter +1;
      remainder = remainder + m;

    #change m
    m = m*2;

  #Add last element to the counter as part of the sum
  counter = counter+1;
  remainder = remainder + m;
  result = [];
  result.append(remainder)
  result.append(counter)
  return (result)

russianMultiply(657,53)

def testCase(testNumber, n,m,expectedResult):
  actualResult = russianMultiply(n,m)
  if actualResult == expectedResult: print('Test',testNumber,'passed.')
  else: print('Test',testNumber,'failed.')

def test():
  testCase(1,53,657,[34821,4])
  testCase(2,50,65,[3250,3])
  testCase(3,1,2,[2,1])
  testCase(4,10,20,[200,2])
  testCase(5,65,50,[3250,2])
  testCase(6,65,67,[4355,2])
  testCase(7,65,65,[4225,2])
  testCase(8,65,100,[6500, 2])

test()