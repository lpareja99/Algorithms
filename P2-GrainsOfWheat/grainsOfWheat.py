#Program: Grains of Wheat
#Class: CSCI 0262
#Professor: Dr. Carol Browning
#Student: Laura Pareja Prieto
#Date: 09/04/2019
#Version: 1.0

# import of math library that will be used later to turn a float in a interger.
import math;

#Fuction to calculate the total grains obtained depending for a certain math fuction and certain nxn matix.
# @myfun = math function to use.
# @dimension = lengh of one matrix side(n)
# @sum = total number of grains 
def numberOfGrains(myfun,dimension):

  #initialize sum to 0, we don't have any grain at the beggining
  sum = 0
  #calculate the range of the total matrix nxn
  maxRange = dimension * dimension
  #add every time whatever the fuction gives us to what we had at the beggining. We do it as      many times as squares are in the matrix
  for k in range(1,maxRange+1):
    sum = sum + myfun(k)
  return (sum)

def testCount():
  print("---> Tests for number of grains <---")
  if numberOfGrains(lambda k:k,10)==5050:
    print ("Test 1 passed. Number of grains with identity function")
  if numberOfGrains(lambda k:k*k,2)==30: 
    print ("Test 2 passed. Number of grains with square function")
  if numberOfGrains(lambda k:k,3)==45:
    print ("Test 3 passed. Number of grains with identity function")
  if numberOfGrains(lambda k:2**(k-1),8)==18446744073709551615:
    print ("Test 4 passed. Number of grains with 2^(k-1) function. Function from #10.a is working,")
  if numberOfGrains(lambda k:2*k-1,3)==81:
    print ("Test 5 passed. Number of grains with k^4 function. Function from #10.b is working,")
  

testCount()

#function to calculate how much time in years, days, hours, minutes and seconds, a function in a specific matrix take long if every grain of wheat is one second.
def timeToCount(myfun,dimension):

  #inital values, how many seconds is a year,day,hour,and minute
  year = 31536000
  day = 86400
  hour = 3600
  minute = 60 

  #call function numberOfGrain to know how many seconds total we have
  secondsLeft = math.floor(numberOfGrains(myfun,dimension))

  #Make respective operations to obtain the numbers
  years =  secondsLeft // year
  secondsLeft = secondsLeft % year
  days = secondsLeft // day
  secondsLeft = secondsLeft % day
  hours = secondsLeft // hour
  secondsLeft = secondsLeft % hour
  minutes = secondsLeft // minute
  seconds = secondsLeft % minute

  print("done")

  #return final values
  return[seconds,minutes,hours,days,years]

def testTime():
  print("---> Test for time <---")
  if timeToCount(lambda k:k,10)==[10,24,1,0,0]:
    print ("Test 1 passed.  Time to count with identity function.")
  if timeToCount(lambda k:k*k,10)==[10,59,21,3,0]:
    print ("Test 2 passed.  Time to count with square function.")
  if timeToCount(lambda k:2**(k-1),8)==[15,0,7,26,584942417355]:
    print ("Test 3 passed. Time to count with identity function. Time counting for #10.a is working.")
  if timeToCount(lambda k:k*2-1,3)==[21,1,0,0,0]:
    print(("Test 4 passed. Time to count with identity function. Time counting for #10.b is working."))

testTime()