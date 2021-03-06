import math
import statistics
import numpy

#this will serve as the main page for the functionality

# use Django to create web interface

# function for basic math

def Add(x, y):
    if isinstance(x, (int, float)) and isinstance(y,(int, float)):
        return x+y
    else:
        results = str(x) + "+" + str(y)
        return results

def Sub(x, y):
    if isinstance(x, (int, float)) and isinstance(y,(int, float)):
        return x-y
    else:
        ans = str(x) + "-" + str(y)
        return ans

def Multiply(x, y):
        return x*y

def Divide(x, y):
        if y==0:
            return "Divide by zero error, try again"
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

#due to float arithmetic things such as sin(pi) !=
#however they are still extremely small numbers could be a way to round it
#for better user experience

def findSin(x, choice):
        if choice == 'R':
            ans = math.sin(x)
        elif choice == 'D':
            ans = math.sin(math.radians(x))    #if degrees is entered converts to radians to compute
        if ans < 0.0000000000001:       #solves rounding error for expected 0 result like sin(pi)
            ans = 0
        elif ans > 0.999999999999:
            ans = 1
        return ans

def findCos(x, choice):
        if choice == 'R':
            ans = math.cos(x)
        elif choice == 'D':
            ans = math.cos(math.radians(x))
        if ans < 0.0000000000001:
            ans = 0
        elif ans > 0.999999999999:
            ans = 1
        return ans

def findTan(x, choice):
        if choice == 'R':
            ans = math.tan(x)
        elif choice == 'D':
            ans = math.tan(math.radians(x))
        if ans < 0.0000000000001:
            ans = 0
        elif ans > 0.999999999999:
            ans = 1
        return ans

def findSec(x, choice):
        if choice == 'R':
            ans = (1/math.cos(x))
        elif choice == 'D':
            ans = (1/math.cos(math.radians(x)))
        if ans < 0.0000000000001:
            ans = 0
        elif ans > 0.999999999999 and ans < 1.0000000000000000000000:
            ans = 1
        return ans

def findCsc(x, choice):
        if x == 0:
            ans = 0
            return ans
        if choice == 'R':
            ans = (1/math.sin(x))
        elif choice == 'D':
            ans = (1/math.sin(math.radians(x)))
        if ans < 0.0000000000001:
            ans = 0
        elif ans > 0.9999999999999999999 and ans < 1.0000000000000001:
            ans = 1
        return ans

def findCot(x, choice):
        if x == 0:
            ans = 0
            return ans
        if choice == 'R':
            ans = (1/math.tan(x))
        elif choice == 'D':
            ans = (1/math.tan(math.radians(x)))
        if ans < 0.0000000000001:
            ans = 0
        elif ans > 0.9999999999999999999 and ans == 1.0000000000000002:
            ans = 1
        return ans

def getPi():
    return numpy.pi

# function for statistics

def findMean(x):
    return statistics.mean(x)

def findMedian(x):
    return statistics.median(x)

def findMode(x):
    return statistics.multimode(x)

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

# function for calculus
def findIndefIntegral(x): #Indefinite Integral
    pass

def findDefIntegral(x): #Definite Integral
    pass

def findDerivative(x):
    pass
