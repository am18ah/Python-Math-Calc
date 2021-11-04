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

# function for pre-calculus

# function for trigonometry

# function for statistics

# function for calculus

# function for linear algebra
