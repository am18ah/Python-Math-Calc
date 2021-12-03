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