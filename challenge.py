#Write a python program that iterates through all the numbers from 2 to 144 (inclusive). 
#If a number is a perfect square, print 'fizz'. If the number is a prime number, print 'buzz'. 
# If the the number is a perfect square and its square-root is a prime number, print 'fizzbuzz'

#whiteboarding below
#Output: none, just print strings based on conditions
#Input: none
#Constraints: iterate through all numbers from 2 to 144, inclusive
#Edge Case: if the number is a perfect square and then it's square
# root is also a prime number, should it print 'fizz' and then 'fizzbuzz'? or just print 'fizzbuzz'?
            
import math

#helper func to determine if a number is prime
def isPrime(num):
    isItPrime = True
    #divide number in half and loop to test
    #if number is less than 3, just return True
    #num will never be one (which is not a prime number) because of the range defined in fizzbuzz
    if num < 3:
        return True
    else:
        for y in range(2, num):
            if num % y == 0:
                isItPrime = False
                break
    return isItPrime


def fizzbuzz():
    for x in range(2,145):
        xisPerfectSquare = False
        #if number is perfect square, print 'fizz'
        if math.sqrt(x).is_integer() == True:
            xisPerfectSquare = True
            print('fizz')
        #check if number is prime num, then print 'buzz'
        #prime numbers are numbers greater than 1 where it can only divide into 1 and itself
        if isPrime(x) == True:
            print('buzz')

        #check if number is a perfect square AND squre root is a prime number, print 'fizzbuzz'
        #check if the square root is a number and not a float
        squareRootOfX = math.sqrt(x)
        if squareRootOfX.is_integer() == True:
            #now check and don't forget to convert to int to check prime status
            if xisPerfectSquare == True and isPrime(int(squareRootOfX)) == True:
                print('fizzbuzz')
fizzbuzz()