'''
*Programming Assignment 10
*Ean Vandergraaf & Laura Pareja
*11/18/2019
*Algorithms
*Making Change
*
*V1
'''

'''
PART B
'''
##method finds the right amount of change based using the greedy algorithm.
##@param amount: the total amount of change needed.
##        denomList: the list of coins values that will be returned.
##@return ans: an array of all the coins needed.
def greedyChange(amount,denomList):

  lenght = len(denomList)
  ans = []
  i = lenght-1
  while(i >= 0):
    while(amount >= denomList[i]):
      amount = amount - denomList[i]
      ans.append(denomList[i])
    i = i-1
  return ans

'''
Part C
'''
##method finds the right amount of change using the dynamic change algorithm. 
##        denomList: the list of coins values that will be returned.
##@return coins: an array of all the coins needed.
def dynamicChange(amount,denominations):

  minCoins = [0 for i in range(amount +1)]
  coinUsed = [0 for i in range(amount +1)]

  for cents in range(amount+1):
    coinCount = cents
    newCoin = 1

    arr = []
    for c in denominations:
      if c<=cents:
        arr.append(c)
        
    for j in arr:
      if (minCoins[cents-j] + 1 < coinCount):
        coinCount = minCoins[cents-j]+1
        newCoin = j
        
    minCoins[cents] = coinCount
    coinUsed[cents] = newCoin

  #obtain coins
  coins = []
  coin2Find = amount
  while coin2Find > 0:
    thisCoin = coinUsed[coin2Find]
    coins.append(thisCoin)
    coin2Find = coin2Find - thisCoin

  coins.reverse()
  return coins

def testCase(testNumber,function,amount,denominations,expectedAnswer):
  answer = function(amount,denominations)
  if answer==expectedAnswer:
    print("Test",testNumber,"passed:",amount, denominations,expectedAnswer)
  else:
    print("Test",testNumber,"failed. Expected: ",expectedAnswer, "Was: ", answer)

def test():
  testCase(1,greedyChange,48, [1,5,10,25],[25,10,10,1,1,1])
  testCase(2,dynamicChange,48, [1,5,10,25],[25,10,10,1,1,1]) 

  testCase(3,greedyChange,30, [1,5,10,25],[25,5])
  testCase(4,dynamicChange,30, [1,5,10,25],[25,5])

  testCase(5,greedyChange,30, [1,10,25],[25,1,1,1,1,1])
  testCase(6,dynamicChange,30, [1,10,25],[10,10,10])
  
  testCase(7,greedyChange,6,[1,3,4],[4,1,1])
  testCase(8,dynamicChange,6,[1,3,4],[3,3])

test()


'''
Greedy algorithm chooses the largest coin possible and rested to the total amount looking to all the coins. This makes that sometimes the algorithm doesn't work in the best way. As a example we can use the test 3 were the minimun required of coins would be 3 (10,10,10). But intead of that the greedy algorithm returns (25,1,1,1,1) becuase it chose first the 25 and then look based on that option. It never considers to go back and eleminate that choice.


Part D
The greedy algorithm will have time complexity of O(m), while the dynamic change algorithm will have a time complexity will have a time complexity of O(nm). The dynamic change algorithm is more practical because it provides an answer with the least amount of coins. Although the greedy algorithm is faster it returns an answer with more coins. 
'''