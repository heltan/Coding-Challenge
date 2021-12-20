#Write a python program that iterates through all the numbers from 2 to 144 (inclusive). 
#If a number is a perfect square, print 'fizz'. If the number is a prime number, print 'buzz'. 
# If the the number is a perfect square and its square-root is a prime number, print 'fizzbuzz'

            
import math

def isPrime(num):
    isItPrime = True
    if num < 3:
        return True
    else:
        for y in range(2, int(math.sqrt(num)) + 1):
            if num % y == 0:
                isItPrime = False
                break
    return isItPrime

def fizzbuzz():
    for x in range(2,145):
        xisPerfectSquare = False
        if math.sqrt(x).is_integer() == True:
            xisPerfectSquare = True
            print('fizz')
        if isPrime(x) == True:
            print('buzz')
        squareRootOfX = math.sqrt(x)
        if squareRootOfX.is_integer() == True:
            if xisPerfectSquare == True and isPrime(int(squareRootOfX)) == True:
                print('fizzbuzz')
fizzbuzz()