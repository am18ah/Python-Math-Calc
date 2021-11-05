import math

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
    if isinstance(x, (int, float)) and isinstance(y,(int, float)):
        return x*y
    else: 
        ans = str(x) + "*" + str(y)   
        return ans

def Divide(x, y):
    if isinstance(x, (int, float)) and isinstance(y,(int, float)):
        return x/y
    else: 
        ans = str(x) + "/" + str(y)   
        return ans

def power(x,y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return math.pow(x,y)
    else:
        ans = str(x)+"^"+str(y)
        return ans
# function for pre-calculus

# function for trigonometry

#due to float arithmetic things such as sin(pi) != 
#however they are still extremely small numbers could be a way to round it
#for better user experience

def findSin(x):
    if isinstance(x, (int, float)):
        return math.sin(x)
    else:
        ans = "sin(" + str(x) +")"
        return ans

def findCos(x):
    if isinstance(x, (int, float)):
        return math.cos(x)
    else:
        ans = "cos(" + str(x) +")"
        return ans

def findTan(x):
    if isinstance(x, (int, float)):
        return math.tan(x)
    else:
        ans = "tan(" + str(x) +")"
        return ans

def findCsc(x):
    if isinstance(x, (int, float)):
        return (1/math.sin(x))
    else:
        ans = "csc(" + str(x) +")"
        return ans

def findSec(x):
    if isinstance(x, (int, float)):
        return (1/math.cos(x))
    else:
        ans = "sec(" + str(x) +")"
        return ans

# function for statistics

def findMean(x):
    pass

def findMedian(x):
    pass

def findMode(x):
    pass

def findMin(x):
    pass

def findMax(x):
    pass

def findStdDev(x):
    pass

def findVar(x):
    pass

# function for calculus
def findIndefIntegral(x): #Indefinite Integral
    pass

def findDefIntegral(x): #Definite Integral
    pass

def findDerivative(x):
    pass

# function for linear algebra
