import math
import statistics
import numpy

#this will serve as the main page for the functionality

# use Django to create web interface

# function for basic math
class mathMethods:
    def Add(x, y):
            return x+y

    def Sub(x, y):
            return x-y

<<<<<<< HEAD
    def Multiply(x, y):
            return x*y

    def Divide(x, y):
            return x/y

    def Power(x,y):
            return x ** y

    def Root(x, y = 2):
        if y == 2:
            return math.sqrt(2)     #square root
        else:
            return x ** (1/y)       #root y

# function for pre-calculus

    def findLog(x, y = 10):
        if y == 10:
            return math.log10(x)        #more accurate than log(x, 10)
        else:
            return math.log(x, y)
    def findln(x):
        return math.log(x)  #no base specification defaults to base e (ln)
=======
def Multiply(x, y):
        return x*y

def Divide(x, y):
        return x/y

def Power(x,y):
        return x ** y

def Root(x, y = 2):
    if y == 2:
        return math.sqrt(2)     #square root
    else:
        return x ** (1/y)       #root y

# function for pre-calculus

def findLog(x, y = 10):
    return math.log(x, y)
def findln(x):
    return math.log(x)  #no base specification defaults to base e (ln)

# function for trigonometry
>>>>>>> save

# function for trigonometry

<<<<<<< HEAD
    def findSin(x, choice):
        if choice == 'R':
            ans = math.sin(x)
        elif choice == 'D':
            ans = math.sin(math.radians(x))    #if degrees is entered converts to radians to compute
        if ans < 0.0000000000001:       #solves rounding error for expected 0 result like sin(pi)
            ans = 0
        return ans

    def findCos(x, choice):
        if choice == 'R':
            ans = math.cos(x)
        elif choice == 'D':
            ans = math.cos(math.radians(x))
        if ans < 0.0000000000001:
            ans = 0
        return ans

    def findTan(x, choice):
        if choice == 'R':
            ans = math.tan(x)
        elif choice == 'D':
            ans = math.tan(math.radians(x))
        if ans < 0.0000000000001:
            ans = 0
        return ans

    def findCsc(x, choice):
        if choice == 'R':
            ans = (1/math.sin(x))
        elif choice == 'D':
            ans = (1/math.sin(math.radians(x)))
        if ans < 0.0000000000001:
            ans = 0
        return ans

    def findSec(x, choice):
        if choice == 'R':
            ans = (1/math.cos(x))
        elif choice == 'D':
            ans = (1/math.cos(math.radians(x)))
        if ans < 0.0000000000001:
            ans = 0
        return ans

    def getPi():
        return numpy.pi

# function for statistics

    def findMean(x):
        return statistics.mean(x)

    def findMedian(x):
        return statistics.median(x)

    def findMode(x):
        return statistics.mode(x)

    def findMin(x):
        return numpy.min(x)
=======
def findSin(x):
        return math.sin(x)

def findCos(x):
        return math.cos(x)

def findTan(x):
        return math.tan(x)

def findCsc(x):
        return (1/math.sin(x))

def findSec(x):
        return (1/math.cos(x))

def getPi():
    return numpy.pi

# function for statistics

def findMean(x):
    return statistics.mean(x)

def findMedian(x):
    return statistics.median(x)

def findMode(x):
    return statistics.mode(x)

def findMin(x):
    return numpy.min(x)

def findMax(x):
    return numpy.max(x)

def findRange(x):
    return numpy.max(x) - numpy.min(x)

def findStdDev(x):
    statistics.stdev(x)

def findVar(x):
    statistics.variance(x)
>>>>>>> save

<<<<<<< Updated upstream
    def findMax(x):
        return numpy.max(x)

    def findRange(x):
        return numpy.max(x) - numpy.min(x)

<<<<<<< HEAD
    def findStdDev(x):
        statistics.stdev(x)

    def findVar(x):
        statistics.variance(x)
=======
def findVar(x):
    statistics.variance(x)
>>>>>>> Stashed changes
=======
def findDerivative(x):
    pass
>>>>>>> save
