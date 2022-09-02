#Program: Anagram
#Class: CSCI 0262
#Professor: Dr. Carol Browning
#Student: Laura Pareja Prieto
#Date: 08/29/2019
#Version: 1.0

# Function to indentify if two given inputs (w1 and w2) and anagrams
def anagram(w1,w2):

  #Step 1: Raplace every capital letter for a lower lower letter and delete every space in both words so both are readables.
  w1 = w1.lower().replace(" ","")
  w2 = w2.lower().replace(" ","")

  #Step 2: While loop 
  #   - Every time we compare the letter on position 0 in w1 with           rest of the letters in w2.
  #   - Whenever the progarm finds a common letter, both are deleted        from each word and the counter return to 0, so we starts            again.
  #   - If any of the letters doesn't match with letter 0 in w1 in          any of the loop ends
  i = 0
  while (i < len(w1)):
    if w1[0] == w2[i]:
      w1 = w1.replace(w1[0],"",1)
      w2 = w2.replace(w2[i],"",1)
      i = 0
    else:
      i = i+1
  #Step 3: after the loop we have two options
  #   - Both w1 and w2 are empty what means they are anagrams
  #   - Words are not empty so there is not an anagram
  if (len(w1) == 0 and len(w2) == 0):
   return True
  else:
    return False

  
#Function to test different couple of words and check if tehy are anagrams
def test():
  testPair(1,'eat','tea',True)
  testPair(2,'Clint Eastwood','Old West Action',True)
  testPair(3,'arranged','deranged',False)
  testPair(4, 'dormitory', 'Dirty room', True)
  testPair(5,'test passed','test failed', False)
  testPair(6,'DeSaMpArAdOr','dEsPaRrAmAdo',True)
  testPair(7,'Conservadora','conversadorA',True)
  testPair(8,'I am going to','pass this class',False)
  testPair(9,'98076','08976',True)
  testPair(10,'a','b',False)
  testPair(11,77,76,False)
  testPair(12,666,666,True)

  
#Function to make sure every test on test() function has pass succesfully the test and has the result expected.
def testPair(testNumber,word1,word2,expected):

  #check if the inputs are both string
  if(type(word1) == str and type(word2) == str):
    if anagram(word1,word2)==expected:
      result = "passed"
    else:
      result = "failed"
    print("Test "+str(testNumber)+"  "+result+":"+ word1+" "+word2+" "+str(expected))
  else:
    print ("ERROR: We are so sorry but I think you maybe introduced some wrong values. Please try again and make sure your two inputs are strings. :)")

#Call to function test(). It runs everything
test()