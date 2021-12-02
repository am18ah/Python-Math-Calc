#test driver for math method functionality
import Main as test
import math

L1 = [1, 2, 3, 4, 5]
L2 = [1, 2, 4, 4, 5]
print (test.Add(3, 'x'))
print(test.findSin(math.pi)) 
print(test.Power(3,2))

print("Testing Trig: ")
print(test.findSin(math.pi)) 
print(test.findCos(0))

print("Testing Stats: ")
print(test.findMin(L1))
print(test.findMedian(L1))
print(test.findMode(L2))
print(test.findRange(L1))