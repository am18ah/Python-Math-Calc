import math
<<<<<<< HEAD
=======
import statistics
<<<<<<< HEAD
>>>>>>> parent of b703804 (Update Main.py)
=======
>>>>>>> parent of b703804 (Update Main.py)

#this will serve as the main page for the functionality

# use Django to create web interfacee

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
    temp = 0
    for i in range(0, len(x)):
        temp = temp + x[i]
    return temp/len(x)

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def findIndefIntegral(x,fx): #Indefinite Integral
    # ex: if f(x) = 2x, 2*x will be passed in
    x = sp.Symbol('x')
    sp.integrate(fx,x)
=======
def findIndefIntegral(x): #Indefinite Integral
    pass
>>>>>>> parent of b703804 (Update Main.py)
=======
def findIndefIntegral(x): #Indefinite Integral
    pass
>>>>>>> parent of b703804 (Update Main.py)
=======
def findIndefIntegral(x): #Indefinite Integral
    pass
>>>>>>> parent of b703804 (Update Main.py)

def findDefIntegral(x): #Definite Integral
    pass

def findDerivative(x):
    pass
