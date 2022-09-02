#############################################
# Project Name: Tweety Bird
# Authors: M. Lehenbauer, L. Pareja, A. Hasnat
# Date: 12/08/2019
# Course: CSCI 0262 - Algorithms
# Purpose: Given a txt file with tweets. Be able to add new tweets to the file and be able to return a list of tweets given a certain hashtag.
# Rules: 
#	- One tweet per line.
#	- Only one hashatg per tweet.
#############################################

###############################################
# ==> GLOBAL VARIABLES <==
###############################################
TABLE_SIZE = 17
counterAdd = 0
counterReturn = 0
###############################################
# ==> CLASS CONSTRUCTORS <==
###############################################

#	Pointers, class to create pointers
#	Inputs: the object it would point to
#	Outputs: none
class Pointer(object):
	def __init__(self, object):
		self.object = object

	#getters
	def getObject(self):
		return self.object

	#setters
	def setObject(self, object):
		self.object = object

#	Hashtag, class that creates a hashtag object
#	Inputs: data (a hashtag), a next which is a Pointer, and a tweet which is a Pointer
class Hashtag(object):
	def __init__(self, data=None):
		self.data = data
		self.next = Pointer(None)
		self.tweet = Pointer(None)

	#getters
	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def getTweet(self):
		return self.tweet

	#setters
	def setNext(self, next):
		self.next = next

#	Tweet, class to create tweet objects
#	Inputs: a tweet data to create the object and a next which is a Pointer
#	Outputs: none
class Tweet(object):
	def __init__(self, data=None):
		self.data = data
		self.next = Pointer(None)

	#getters
	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	#setters
	def setNext(self, next):
		self.next = next


###############################################
# ==> SECONDARY FUNCTIONS <==
###############################################

#   getUniqueHash, a function that gets you a list of unique hashtags
#   inputs: none
#   outputs: array with hash tags
def getUniqueHash():
	file = [line.rstrip('\n') for line in open('input.txt')]
	#set up temp array populated with none
	temp = [None] * len(file)	
	#append hashes from file into array slots
	for i in range(0, len(file)):	
		temp[i] = parseHash(file[i])
	#weeds out non-unique hashtags and creates list
	hashtags = list(set(temp))	
	return hashtags

#   parseHash, a function that gets you a hashtag from a line of text
#   inputs: a tweet
#   outputs: hash tag from that tweet
def parseHash(substr):
	#inits indexes for start and end
	start = None
	end = None
	#moves start until it finds start of tweet
	for i in range(0, len(substr)):	
		if (substr[i] == '#'):
			start = i
	#if there's no hash, ends.
	if (start == None): return None	
	#moves end until it finds end of hashtag
	for j in range(start, len(substr)):	
		if (substr[j] == ' '):
			end = j
			break
	#returns end of string as hashtag presumably ends there.
	if (end == None): end = len(substr)	
	#returns hashtag using indexes.
	return substr[start:end]	

#   value, a function to assign a hash number to a hash tag
#   size of the table = 17
#   input: hashtag
#   output: hash value
def value(hashtag):
	hashValue = 0
	#obtain value usin ASCII table and addede to get final value 
	for i in range(0, len(hashtag)):
		hashValue += ord(hashtag[i])
	#obtain hash value = pointer to the table
	hashValue = hashValue % TABLE_SIZE
	return hashValue

#	initList, a function that makes a list with an empty pointer in every index
#	input: None
#	output: a list of pointer objects
def initList():
	pointers = []
	#add a new entry and a new pointer as many times as big the table is going to be
	for i in range(0, TABLE_SIZE):
		pointers.append(Pointer(None))
	return pointers

#	includeTags, a function that connects the hashtags to the hash table
#	input: the list from initList, hashtags from getUniqueHash, and the values of each Hashtag
#	output: the hash table with hashtags added 
def includeTags(nlist, hashtags, hashValues):
	#include one hashtag at the time
	for i in range(0, len(hashtags)):
		newHash = Hashtag(hashtags[i])
		#get the empty pointer next from newHash
		pointerNext = newHash.getNext()
		#fill pointer next with the old first hash object
		pointerNext.setObject(nlist[hashValues[i]].getObject())
		nlist[hashValues[i]].setObject(newHash)
	return nlist

# 	includeTweets, function that connects the tweets to the right hashtag inside the hash table
#	input: hash table
#	outputs: hash table with tweets in it
def includeTweets(llist):
	file = [line.rstrip('\n') for line in open('input.txt')]
	global counterAdd
	#include one tweet at the time
	for tweet in range(0, len(file)):
		#obtain hashtag and hashValue from the hashtag
		hashtag = parseHash(file[tweet])
		hashValue = value(hashtag)

		#.create a new tweet object
		newTweet = Tweet(file[tweet])
		
		#.get the hashtag object were we wanna attach
		hashObj = llist[hashValue]
		actualHash = hashObj.getObject()
		while (True):
			if ((actualHash.next.getObject() != None)
			    and (actualHash.getData() != hashtag)):
				#increment counter
				counterAdd += 1
				pointerNext = actualHash.getNext()
				nextHash = pointerNext.getObject()
				actualHash = nextHash
			else:
				break
			

		# include new tweet in right possition
		pointerTweet = actualHash.getTweet()
		oldTweet = pointerTweet.getObject()
		pointerTweet.setObject(newTweet)
		newTweet.setNext(oldTweet)

	return llist

#	hashTable, afunction that creates a hash table
#	input: None
#	output: The complete hash table 
def hashTable():

	#create empy array with pointers
	pointers = initList()

	#get hashtags from txt file
	hashtags = getUniqueHash()

	#obtain hash values from hashtags
	hashValues = [0] * len(hashtags)
	for i in range(0, len(hashtags)):
		hashValues[i] = value(hashtags[i])

	#include hashtags on the table
	pointers = includeTags(pointers, hashtags, hashValues)

	#include tweets on the table
	pointers = includeTweets(pointers)

	return pointers

###############################################
# ==> ADD TWEET <==
###############################################
#	userWrite, a function that allows a user to write a tweet to be put in a database of tweets
# inputs: none, but the user inputs a Tweet
# outputs: None, but the Tweet is written into our database
def userWrite():
	substr = input('Enter a tweet:	')

	if ((substr == None) or (parseHash(substr) == None)):
		print('Invalid data, aborting.')
		return None

	hashCounter = 0
	for i in range(0, len(substr)):
		if (substr[i] == '#'): hashCounter += 1
		if (hashCounter >= 2):
			print('Too many hashtags, aborting.')
			return None

	if (hashCounter == 1):
		with open("input.txt", "a") as userAdd:
			# add tweet to the file
			userAdd.write('\n' + substr)
		return 0
	else: return None


###############################################
# ==> RETURN TWEET <==
###############################################

#	userSearch, a function that allows a user to search for all the tweets with the same Hashtag
#	inputs: none, but the user is prompted to input a Hashtag
#	outputs: none, but a list of tweets is printed
def userSearch():
	#return hashtag
	substr = parseHash(input('Enter a hashtag:	'))	
	print(" ")
	#gets all the hashes present in the input file
	uniqueHash = getUniqueHash()
	#checks if user inputted hashtag is present	
	if (substr in uniqueHash):	
		if (substr != None):
			#gets all the tweets corresponding to the hashtag
			output = returnTweets(substr)	
			#prnt the tweets
			if (output != None):	
				print('We found the following tweets in our database: \n', output)
				return None
			#if no tweets exist, print error
			else:	
				print('Tweet not found.')
			return 0
		#if does not qualify as a tweet
		else:	
			print('Invalid data entered.')
			return 0
	#if tweet does not exist
	else:	
		print('Tweet is not in database')
		return 0
		
#	returnTweets, a function that gets all the tweets for a Hashtag
#	inputs: a Hashtag
#	outputs: a list of tweets
def returnTweets(hashtag):
	global counterReturn
	output = []

	#create open hash table
	table = hashTable()

	#obtain hashvalue from hashtag
	hashValue = value(hashtag)
	
	#obtain initial possition to add hashtag
	hashObj = table[hashValue]
	actualHash = hashObj.getObject()

	if hasattr(actualHash, 'next'):
		#increment counter
		counterReturn += 1

		#get the possition of the hashtag we are looking for
		while ((actualHash.next.getObject() != None) and (actualHash.getData() != hashtag)):
			#increment counter
			counterReturn += 1
			pointerNext = actualHash.getNext()
			nextHash = pointerNext.getObject()
			actualHash = nextHash
			
	#check if there is any tweet attached to the hashtag
	if hasattr(actualHash, 'tweet'):
		actualTweet = actualHash.tweet.getObject()
	else: return None

	#return all tweets attached to the hashtag
	while ((actualTweet != None)):
		if ((hasattr(actualTweet, 'getData'))): output.append(actualTweet.getData())
		counterReturn += 1
		pointerTweet = actualTweet.getNext()
		actualTweet = pointerTweet

	#if we return tweets then return the output and reset counter
	if (output != []):
		#print("Number of comparisons to return tweets: ",counterReturn)
		print(" ") 
		return output
	

###############################################
# ==> MAIN FUNCTION <==
###############################################

def main():
	global counterReturn
	global counterAdd
	print('#####################################################')
	print('#####Welcome to TweetDB, a basic tweet database.#####')
	print('#####################################################')
	print('')
	print(
	    'Type add to add a tweet, or type return to return the tweets we stored.'
	)
	print('')
	#gets user input for which function to run
	cin = input()	
	#user selects adding tweets
	if (cin == 'add'):	
		#declare empty substring
		substr = None
		#populate substring by feeding status from userWrite
		substr = userWrite()
		#check for status
		if (substr != None):	
			print('Tweet has been added to database.')
			print('')
			
	#user selects return function
	elif (cin == 'return'):
		#set up status counter	
		check = 0	
		#do function while not done
		while (check == 0):	
			check = userSearch()
		print("Number of comparisons ==>")
		print("# comparisons to add a tweet(last tweet): ",counterAdd)
		print("# comparisons to return all tweet with same hashtags: ",counterReturn)
	else:
		#if invalid print error
		print('ERR: Invalid Input')	
	print('')
	#resets counters because Python
	counterReturn = 0
	counterAdd = 0
	print(" ")
	print('########This program is now exiting. Goodbye.########')

	return None

###############################################
# ==> TEST <==
###############################################

#tests(): funtion to test different possibilities and make sure the program is working
# no inputs
# Outputs: if the test case pass the test
def test():
	testCase(1,"add","hi my name is #name","Tweet has been added to database.") 
	testCase(2,"return","#name","hi my name is #name")
	testCase(3,"return","#noName","Tweet is not in database")
	testCase(4,"add","hi #bye #hi","Too many hashtags, aborting.")
	testCase(5,"add","hi bye","Invalid data, aborting")

#testCase(): function to evaluate an spefic case from tets() function
# Inputs:
#   - testNumber: number assigned the the test
#   - puzzle: array with the operation wrote with characters
#   - digits: an array with the numbers to use
#   - expectedList: a list with possible solutions
# Outputs: print if the test passed or not.
def testCase(testNumber,action,hashTagOrTweet,expectedResult):
	main()
	print ("Test",testNumber,"check above to see if expect result matches")
	print(action,expectedResult)