# Name: Cryptarithm Solver
# Author: Laura Pareja Prieto
# Date: 10/03/19
# Course: CSCI 0262 - Algorithms
# Purpose: Given a puzzle using four digits figure out which number goes for which digit to solve the cryptarithm.
# Modification log: 1.0

# solve(), main method to solve a cryptarithm.
# Inputs:
#   - puzzle: Array with letter operations ex:[a,b,cd]
#   - digitList: Array with numbers for digits ex:[1,2,6,8]
# Outputs:
#   - result: string with the operation. Ex: "5+5=10"
def solve(puzzle,digitList):
  # number for diferent characters in the operation
  NUMS2ASSING = 4;
  # array to keep the 4 lettersArr we are going to use
  lettersArr = [];

  # Obtain letters and put them inside lettersArr array
  for i in range(0,len(puzzle)):
    string = puzzle[i];
    for letter in range(0,len(string)):
      if string[letter] in lettersArr:
        letter = letter+1;
      else:
        lettersArr.append(string[letter]);
        letter = letter+1;

  # Check with the different options
  operationArr = [];
  end = len(digitList)-1;
  while (end >= 1):
    for j in range(0,end):

      # to loop through a whole round, only move right elements
      for i in range (0,NUMS2ASSING):
        # Convert puzzle from letters to digits
        operationArr = convertLetter2Num(puzzle,digitList,lettersArr);

        #call function to swipe all numbers one position rigth
        digitList = moveRight(digitList);

        if(int(operationArr[0]) + int(operationArr[1]) == int(operationArr[2])):
          result = operationArr[0] + "+" + operationArr[1]  + "=" + operationArr[2];
          return (result);
        else:
          #call function to swipe all numbers one position rigth
          digitList = moveRight(digitList);

      # change position j and position j+1 one with other
      pos1 = j;
      pos2 = j+1;
      digitList = changeDigList(digitList,pos1,pos2);
  

#moveRight(): function to move all digits in an array one possition right and put the last value at the beginning.
# Input:
#   - digitList: an array with elements.
# Outputs:
#   - newList: an array with numbers
def moveRight(digitList):
  newList = [digitList[3],digitList[0],digitList[1],digitList[2]];
  return newList

#changeDigList(): function to swap two specific positions in a array.
# Inputs:
#   - digitList: an array with elements
#   - pos1: position for the first element to swap
#   - pos2: position for the second element to swap
# Outputs:
#   - digitList: an array with elements.
def changeDigList(digitList,pos1,pos2):
  temp = digitList[pos1];
  digitList[pos1] = digitList[pos2];
  digitList[pos2] = temp;
  return (digitList);

#convertLetter2Num():  function to assing the right number to every character in the operation.
# Inputs:
#   - puzzle: an array with the operation wrote with characters
#   - digitList: and array with the numbers we are using
#   - lettersArr: an array with the characters we are using
# Outputs:
#   - operationArr: an array with the operation wrote with numbers
def convertLetter2Num(puzzle,digitList,lettersArr):
  operationArr = [];
  for i in range(0,len(puzzle)):
    string = puzzle[i];
    number = "";
    for j in range(0,len(string)):
      numIndex = lettersArr.index(string[j]);
      number = number + str(digitList[numIndex]);
    operationArr.append(number);
  return(operationArr)

#tets(): funtion to test different possibilities and make sure the program is working
# no inputs
# Outputs: if the test case pass the test
def test():
  testCase(1,['a','b','cd'],[1,4,6,8],["6+8=14","8+6=14"])
  testCase(2,['q','r','st'],[5,2,1,7],["5+7=12","7+5=12"])
  testCase(3,['xyz','zx','xzw'],[4,7,0,3],["304+43=347","403+34=437"])
  testCase(4,['a','b','cd'],[5,5,1,0],["5+5=10"])
  testCase(5,['aa','b','cdc'],[2,1,0,9],["99+2=101"])
  testCase(6,['a','b','cd'],[1,7,8,9],["8+9=17","9+8=17"])
  testCase(7,['ab','cb','db'],[0,1,2,3],["20+10=30","10+20=30"])
  testCase(8,['aa','bc','da'],[7,1,0,8],["77+10=87"])

#testCase(): function to evaluate an spefic case from tets() function
# Inputs:
#   - testNumber: number assigned the the test
#   - puzzle: array with the operation wrote with characters
#   - digits: an array with the numbers to use
#   - expectedList: a list with possible solutions
# Outputs: print if the test passed or not.
def testCase(testNumber,puzzle,digits,expectedList):
  actualResult = solve(puzzle,digits)
  if actualResult in expectedList: print ("Test",testNumber,"passed.")
  else: print ("Test",testNumber,"failed.  Expected one of: ",expectedList," Actual: ",actualResult)

#call the function
test()