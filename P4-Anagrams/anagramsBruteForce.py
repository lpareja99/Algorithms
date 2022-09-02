#Program: Anagram
#Class: CSCI 0262
#Professor: Dr. Carol Browning
#Student: Laura Pareja Prieto
#Date: 08/29/2019
#Version: 1.0

#Algorithm for Brute Force String Matching on page 105
# - Inputs: LongText,searchString
# - Outputs: posTxt or -1(if no positon found)
def BruteForceStringMatch(longText,searchString):

  #Get distance from both Strings
  distTxt = len(longText);
  distStr = len(searchString);

  #check every position in the longText to see if any letter matches with first letter in searchString
  for posTxt in range(0,distTxt - distStr):
    posStr = 0;

    #if we find a match, check if the rest of the letter matches, if so, return position where first letter of searchString matches with longText.
    while (posStr < distStr and searchString[posStr] == longText[posTxt + posStr]):
      posStr = posStr +1;
    if posStr == distStr:
      return posTxt
  return -1

#Algorithm to realize test case on BruteForceStringMatch algorithm.
def testCaseA(testNumber,longText,searchString,expectedResult):
  actualResult = BruteForceStringMatch(longText,searchString)
  if actualResult == expectedResult: 
    print ("Test",testNumber,"passed.")
  else: 
    print ("Test",testNumber,"failed.  Expected",expectedResult, "but found",actualResult)


def testA():
  testCaseA(1,"Oh I wish I were an aardvark.","were",12) 
  testCaseA(2,"Oh I wish I were an aardvark.","join",-1) 
  testCaseA(3,"She sells sea shells by the seashore.","seashore",28)
  testCaseA(4,"Laura fue a la casa de Manolo en busca de una habichuelas","busca",33)
  testCaseA(5,"This test should be negative","positive",-1)
testA()

#Change this copy to include a counter for the number of character comparisons made.  Your new function returns a list where the first element is the position of the first letter of the first occurrence of the search string in the text, and the second element is the number of comparisons made.

#Algorith to check the number of comparisons the algorithm in part A made 
def BruteForceCounter(longText,searchString):

  #Get distance from both Strings
  distTxt = len(longText);
  distStr = len(searchString);

  #inizialize counter
  counter = 0;
  result = [1]*2; 

  #check every position in the longText to see if any letter matches with first letter in searchString
  for posTxt in range(0,(distTxt - distStr)+1):
    posStr = 0;

    #if we find a match, check if the rest of the letter matches, if so, return position where first letter of searchString matches with longText.
    
    while (posStr < distStr and searchString[posStr] == longText[posTxt + posStr]):
      #counter goes inside, if not it would count one comparison more that it should.
      counter = counter + 1;
      posStr = posStr + 1;
    
    if posStr == distStr:
      result[0] = posTxt;
      result[1] = counter;
      #print(posTxt)
      #print(counter)
      return result
    counter = counter +1;
  result[0] = -1;
  result[1] = counter;
  return result
 
#Algorithm to realize test case on BruteForceCounter algorithm.
def testCaseB(testNumber,longText,searchString,expectedResult):
  actualResult = BruteForceCounter(longText,searchString)
  if actualResult == expectedResult: 
    print ("Test",testNumber,"passed.")
  else: 
    print ("Test",testNumber,"failed.  Expected ",expectedResult, "but found",actualResult)
    #print ("Test",testNumber,"failed.  Expected",expectedResult, "but found",actualResult)


def testB():
  testCaseB(1,"0000","1",[-1,4]) 
  testCaseB(2,"rosalia","al",[3,5])
  testCaseB(3,"rasalia","al",[3,6])
  testCaseB(4,"000000","11",[-1,5])
  testCaseB(5,"THERE_IS_MORE_TO_LIFE_THAN_INCREASING_ITS_SPEED","GHANDI",[-1,43])
  testCaseB(6,"0000001","001",[4,15])
  testCaseB(7,"00000000000000000001","00001",[15,80])
  testCaseB(8,"hola caracola","hola",[0,4])
  testCaseB(9,"Oh I wish I were an aardvark.","were",[12,17]) 
  testCaseB(10,"Oh I wish I were an aardvark.","join",[-1,26]) 
  testCaseB(11,"She sells sea shells by the seashore.","seashore",[28,44])
  testCaseB(12,"Laura fue a la casa de Manolo en busca de una habichuelas","busca",[33,38])
  testCaseB(13,"This test should be negative","positive",[-1,21])
testB()