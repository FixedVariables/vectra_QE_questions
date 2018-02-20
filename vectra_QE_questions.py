from math import sqrt
#import pytest


"""
# Original version; self-sustaining without lsPrimes call

def isPrime(n):
    if isinstance(n, int):
        try:
            n = abs(n)
            for divisor in range(2, int(sqrt(n))+1):
                print "%d modulo %d is %d" % (n, divisor, n%divisor)
                if n % divisor == 0:
                    print "Number is Composite"
                    return False
            print "Number is Prime"
            return True
        except:
            print "Unknown Error" #this should never occur
            return False

    print "Input Type Error; please use an integer"
    return False
"""

# Return a list of all prime numbers less than or equal to the input, n
def lsPrimes(n, plist=[2], start=3):
    for i in range(start, n+1):
        test = True
        for prime in plist:
            #print "testing %d" % i
            if i % prime == 0:
                #print ">>divisible by %d" % prime
                test = False
            #print "%d is prime, %d is i" % (prime, i)
        if test:
            plist.append(i)
    #print plist
    return plist

# Returns True if input is a prime integer; False for all other input
def isPrime(n):
    if isinstance(n,int):
        return abs(n) in lsPrimes(abs(n))
    #print "Input error. Please enter an integer."
    return False


# Prints out list of primes starting at 1, though 1 is not technically prime
def printPrimes(n):
    curr = 3
    plist = [2]
    while len(plist) < n-1:
        plist = lsPrimes(curr+1, plist, curr)
        curr += 1
    plist = [1] + plist
    for num in plist:
        print num
    #print plist # To print the list of primes
    #return plist # To return the list of primes

def isPalindrome(word):
    if not(isinstance(word, str)):
        return False
    a = 0
    b = len(word)
    while a < b-1:
        if word[a] != word[b-1]:
            return False
        a += 1
        b -= 1
    return True


def test_isPalindrome():
    falseCases = (-3, 7.7, 101, "garg", 'ab', "%n")
    trueCases = ("racecar", 'a', "1001", "@=@")
    for case in falseCases:
        assert isPalindrome(case) == False
    for case in trueCases:
        assert isPalindrome(case) == True

def test_isPrime():
    falseCases = (49, 'a', 3.75, sqrt(3), [], {'g':5},[((0))])
    trueCases = (47, -499)
    for case in falseCases:
        assert isPrime(case) == False
    for case in trueCases:
        assert isPrime(case) == True


test_isPrime()
test_isPalindrome()
#printPrimes(5000)