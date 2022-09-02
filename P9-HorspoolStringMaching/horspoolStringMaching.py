'''
*Programming Assignment 9
*Ean Vandergraaf & Laura Pareja
*11/8/2019
*Algorithms
*Horspool String Matching
*7.2
*V1
'''

'''
PART B
'''
##method finds the shift table in alphabetical order of all the letters in the pattern.
##@param pattern: a string that will be used to find in a text.
##@return table: the dictionary of every letter in the pattern and their distance from the last letter.
def shiftTable(pattern):
  alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1"]
  table = {}
  pattern = pattern.lower()
  length = len(pattern)

  
  for letter in alphabet:
    if((letter not in table) and (letter in pattern)):
      
      pos = findLast(pattern, letter)
      if(pos != -1):
        table[letter] = length - pos

  return table

##method finds the first occurance of a letter in a pattern from the left to the right
##@param pattern: the string that will be searched.
##       letter: the letter that is being searched for.
##@return i: the index of the letter, -1 if not found.
def findLast(pattern, letter):
  i = len(pattern)
  while(i > 0):
    if(pattern[i-2] == letter):
      return i-1
    i = i - 1
  return -1

  
def shiftTestCase(testNum,pattern,answer):
  result = shiftTable(pattern)
  if result == answer:
    print ('Test',testNum,'passed')
  else:
    print ('Test',testNum,'failed.  Expected',answer,'but returned',result)

def testShiftTable():
  shiftTestCase(1,"barber",{'a': 4, 'b': 2, 'e': 1, 'r': 3})
  shiftTestCase(2,"leader",{'a': 3, 'd': 2, 'e': 1, 'l': 5, 'r': 6})
  shiftTestCase(3,"reorder",{'d': 2, 'e': 1,'o': 4, 'r': 3})
  shiftTestCase(4,"TCCTATTCTT",{'a': 5,'c': 2,'t': 1})

testShiftTable()

'''
PART C
'''

##method finds the first index of the pattern in the text implementing the Horspool algorithm with a shift table.
##@param pattern: a string of length m that will be searched for in a string of length m.
##       text: a string of length n that may or may not contain the                  pattern. 
##@return resultArr[]: the array containing the first index of the pattern in the text, -1 if not found, followed by the amount of key comparisons by the algorithm.
def HorspoolMatching(pattern,text):
  count = 0

  resultArr = []

  table = shiftTable(pattern)
  ##the pattern array
  pArr = list(pattern)
  ##the text array
  tArr = list(text)

  m = len(pattern)
  n = len(text)
  i = m - 1
  
  while (i <= n-1):
    k = 0
  
    while((pArr[m-1-k] == tArr[i-k]) and (k <= m-1)):
      count = count + 1
      k = k + 1
     
    ##found the pattern in the string
    if(k == m):
      resultArr.append(i-m+1)
      resultArr.append(count)
      return resultArr
    ##jumps down the text
    else:
      a = tArr[i]
      count = count + 1
      if(a in pArr):
        i = i + table[a]
      else:
        i = i + m

  resultArr.append(-1)
  resultArr.append(count)    
  return resultArr


def testCaseH(testNumber, string, text,expectedResult):
  actualResult = HorspoolMatching(string,text)
  if actualResult == expectedResult:
    print ("Test",testNumber,"passed.")
  else:
    print ("Test",testNumber,"failed.  Expected",expectedResult, "but found",actualResult)

def testHorspool():
  #testCaseH (5, "barber","jim saw me in a barbershop",16) #without the counter
  testCaseH (5, "barber","jim saw me in a barbershop",[16,12]) 
  #with the counter
  testCaseH(6, "were","Oh I wish I were an aardvark.",[12,7]) 

  testCaseH(7, "join","Oh I wish I were an aardvark.",[-1,7])

  testCaseH(8, "seashore","She sells sea shells by the seashore.",[28,14]) 
  
  testCaseH(9, "00001","0"*1000,[-1,996])
  testCaseH(10,"10000","0"*1000,[-1,4980])
  testCaseH(11,"01010","0"*1000,[-1,996])
  testCaseH(12,"a"+"b"*100,"b"*1000,[-1,90900])
  testCaseH(13,"00000","0"*1000,[0,5])
  testCaseH(14,"10000","0"*95+"10000",[95,461])

testHorspool()