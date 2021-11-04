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

# function for calculus

# function for linear algebra
