#Write a python program that iterates through all the numbers from 2 to 144 (inclusive). 
#If a number is a perfect square, print 'fizz'. If the number is a prime number, print 'buzz'. 
# If the the number is a perfect square and its square-root is a prime number, print 'fizzbuzz'

#whiteboarding below
#Output: none, just print strings based on conditions
#Input: none
#Constraints: iterate through all numbers from 2 to 144, inclusive
#Edge Case: none
import math
def fizzbuzz():
    for x in range(2,145):

        #if number is perfect square, print 'fizz'
        if math.sqrt(x).is_integer() == True:
            print(x)
            print('fizz')
        #check if number is prime num, then print 'buzz'

        #check if number is a perfect square AND squre root is a prime number, print 'fizzbuzz'

fizzbuzz()