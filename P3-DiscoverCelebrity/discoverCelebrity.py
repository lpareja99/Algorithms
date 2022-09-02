#Debug in case necessary
DEBUG = False

#This function runs a test case for the given test number, adjacency matrix, and expected result.  
def testCaseCeleb(testNumber,adjMatrix,expectedResult):
  actualResult= findCeleb(adjMatrix)
  if actualResult==expectedResult:
    print ("Test", testNumber,"passed.")
  else:
    print ("Test", testNumber,"failed.  Expected ",expectedResult,"but found",actualResult)



#This function runs a suite of tests.  
def test():					
  testCaseCeleb(1,[[0,1,1],[0,0,0],[1,1,0]],1) 
  testCaseCeleb(2,[[0,0,1],[0,0,0],[1,1,0]],-1) 
  testCaseCeleb(3,[[0,1,1],[0,0,1],[1,1,0]],-1) 
  testCaseCeleb(4,[[0,1,0],[0,0,1],[1,0,0]],-1)



#import array

# This function finds the celebrity if there is one in the given adjacency matrix.  
# The input is the adjacency matrix and the output is the celebrity number 
# or -1 if no celebrity is present.  
def findCeleb(adjMatrix):
  if (DEBUG):
  	print(adjMatrix)
  matrixSize = len(adjMatrix)

  #create an array with 
  #checkListFinal = []
  #for i in range(0,matrixSize):
  #  checkListFinal.append(0)
  #  print(checkListFinal[i])

  chance = False
  posCel = False
  possibleRow = 0
  
  if (DEBUG):
    print("going througt the matrix and comparing...")

  for i in range(0,matrixSize):
    chance = False
    checkList = []
 
    for j in range(0,matrixSize):

	  if (DEBUG):
      	print("row")
      	print(j)
      if (adjMatrix[i][j] == 1):
        chance = True
        checkList.append(0)
		if(DEBUG):
        	print(True)
        	print(checkList)

    if chance == True and len(checkList) == matrixSize:
      posCel = True
      possibleRow = i
      print("possible")
      print(i)
    
  print(chance)
  print(posCel)

  if posCel == True:
    adjMatrix[possibleRow][possibleRow] = 0
    print(adjMatrix)

    celebrity = True
    for i in range (0,matrixSize-1):
      if (adjMatrix[posCel][i] == 0):
        celebrity = False
        return (-1)
      else:
        celebrity = True

      return(1)

   # if celebrity == True:
   #  return (celebrity)
   #  print(celebrity)
    # else:
    #  return (celebrity)
    # print(celebrity)
    
  else:
    return(-1)


test()