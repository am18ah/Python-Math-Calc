#test driver for math method functionality
import Main as test
import math

L1 = [1, 2, 3, 4, 5]
L2 = [1, 2, 4, 4, 5] 
print(test.mathMethods.Power(3,2))

print("Testing Trig: ")
print(test.mathMethods.findSin(math.pi, 'R')) 
print(test.mathMethods.findCos(0, 'R'))
print(test.mathMethods.findCos(90, 'D'))

print("Testing Stats: ")
<<<<<<< Updated upstream
print(test.mathMethods.findMin(L1))
print(test.mathMethods.findMedian(L1))
print(test.mathMethods.findMode(L2))
print(test.mathMethods.findRange(L1))
=======
print(test.findMin(L1))
print(test.findMedian(L1))
print(test.findMean(L1))
print(test.findMode(L2))
print(test.findRange(L1))
>>>>>>> Stashed changes
