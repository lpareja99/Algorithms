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
file = [line.rstrip('\n') for line in open('input.txt')]
TABLE_SIZE = 17

###############################################
# ==> CLASS CONSTRUCTORS <==
###############################################

# solve(), main method to solve a cryptarithm.
# Inputs:
#   - puzzle: Array with letter operations ex:[a,b,cd]
#   - digitList: Array with numbers for digits ex:[1,2,6,8]
# Outputs:
#   - result: string with the operation. Ex: "5+5=10"
class Pointer(object):
	def __init__(self, object):
		self.object = object

	def get_object(self):
		return self.object

	def set_object(self, object):
		self.object = object

class Hashtag(object):
	def __init__(self, data=None):
		self.data = data
		self.next = Pointer(None)
		self.tweet = Pointer(None)

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, next):
		self.next = next

	def get_tweet(self):
		return self.tweet

class Tweet(object):
	def __init__(self, data=None):
		self.data = data
		self.next = Pointer(None)

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, next):
		self.next = next


###############################################
# ==> SECONDARY FUNCTIONS <==
###############################################

#   getUniqueHash, a function that gets you a list of unique hashtags
#   inputs: none
#   outputs: array with hash tags
def getUniqueHash():

	temp = [None] * len(file)

	for i in range(0, len(file)):
		temp[i] = parseHash(file[i])

	hashtags = list(set(temp))
	return hashtags

#   parseHash, a function that gets you a hashtag from a line of text
#   inputs: a tweet
#   outputs: hash tag from that tweet
def parseHash(substr):

	start = None
	end = None

	for i in range(0, len(substr)):
		if (substr[i] == '#'):
			start = i
	if (start == None): return None

	for j in range(start, len(substr)):
		if (substr[j] == ' '):
			end = j
			break
	if (end == None): end = len(substr)

	return substr[start:end]

#   value, a function to assign a hash number to a hash tag
#   size of the table = 17
#   input: hashtag
#   output: hash value
def value(hashtag):

	hashValue = 0

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
	for i in range(0, TABLE_SIZE):
		pointers.append(Pointer(None))

	return pointers

#	includeTags, a function that connects the hashtags to the hash table
#	input: the list from initList, hashtags from getUniqueHash, and the values of each Hashtag
#	output: the hash table with hashtags added 
def includeTags(nlist, hashtags, hashValues):

	for i in range(0, len(hashtags)):

		#1.create a new hashtag object
		newHash = Hashtag(hashtags[i])
		#2.get the empty pointer next from newHash
		pointerNext = newHash.get_next()
		#3.fill pointer next with the old first hash object
		pointerNext.set_object(nlist[hashValues[i]].get_object())

		nlist[hashValues[i]].set_object(newHash)

	return nlist

# 	includeTweets, function that connects the tweets to the right hashtag inside the hash table
#	input: hash table
#	outputs: hash table with tweets in it
def includeTweets(llist):

	for tweet in range(0, len(file)):

		hashtag = parseHash(file[tweet])
		hashValue = value(hashtag)

		#1.create a new tweet object
		newTweet = Tweet(file[tweet])
		#2.get the hashtag object were we wanna attach

		hashObj = llist[hashValue]
		actualHash = hashObj.get_object()
		while (True):
			if ((actualHash.next.get_object() != None)
			    and (actualHash.get_data() != hashtag)):
				pointerNext = actualHash.get_next()
				nextHash = pointerNext.get_object()
				actualHash = nextHash
			else:
				break
			#print("nextapp: ",actualHash.get_data()

		#3. include new tweet in right possition
		pointerTweet = actualHash.get_tweet()
		oldTweet = pointerTweet.get_object()
		pointerTweet.set_object(newTweet)
		newTweet.set_next(oldTweet)

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
		#print(hashtags[i])
		hashValues[i] = value(hashtags[i])

	#include hashtags on the table
	pointers = includeTags(pointers, hashtags, hashValues)

	#include tweets on the table
	pointers = includeTweets(pointers)

	return pointers

#	userSearch, a function that 
def userSearch():

	#return hashtag
	substr = parseHash(input('Enter a hashtag:	'))
	uniqueHash = getUniqueHash()
	if (substr in uniqueHash):
		if (substr != None):
			output = returnTweets(substr)
			if (output != None):
				print('We found the following tweets in our database: \n', output)
				return None
			else:
				print('Tweet not found.')
			return 0
		else:
			print('Invalid data entered.')
			return 0
	else:
		print('Tweet is not in database')
		return 0

###############################################
# ==> ADD TWEET <==
###############################################

def userWrite():

	substr = input('Enter a tweet:	')

	if ((substr == None) or (parseHash(substr) == None)):
		print('Invalid data, aborting.')
		return None

	hashCounter = 0
	for i in range(0, len(substr)):
		if (substr[i] == '#'): hashCounter += 1
		if (hashCounter >= 2):
			print('Too many tweets, retry.')
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

def returnTweets(hashtag):

	output = []
	table = hashTable()
	hashValue = value(hashtag)

	hashObj = table[hashValue]
	actualHash = hashObj.get_object()

	if hasattr(actualHash, 'next'):
		while ((actualHash.next.get_object() != None) and (actualHash.get_data() != hashtag)):
			pointerNext = actualHash.get_next()
			nextHash = pointerNext.get_object()
			actualHash = nextHash

	if hasattr(actualHash, 'tweet'):
		actualTweet = actualHash.tweet.get_object()
	else: return None

	while ((actualTweet != None)):
		if ((hasattr(actualTweet, 'get_data'))): output.append(actualTweet.get_data())
		pointerTweet = actualTweet.get_next()
		actualTweet = pointerTweet

	if (output != []): return output

###############################################
# ==> MAIN FUNCTION <==
###############################################

def main():

	print('#####################################################')
	print('#####Welcome to TweetDB, a basic tweet database.#####')
	print('#####################################################')
	print('')
	print(
	    'Type add to add a tweet, or type return to return the tweets we stored.'
	)
	print('')

	cin = input()

	if (cin == 'add'):
		substr = None
		while (substr == None):
			substr = userWrite()
		if (substr != None):
			print('Tweet has been added to database.')
			print('')
	elif (cin == 'return'):
		check = 0
		while (check == 0):
			check = userSearch()
	else:
		print('ERR: Invalid Input')
	print('')

	print('########This program is now exiting. Goodbye.########')
	return None