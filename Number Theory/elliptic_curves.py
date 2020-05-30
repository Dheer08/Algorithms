'''
Given two points (x1,y1),(x2,y2) find the other point (x3,y3) in an elliptic curve y2 = x3 + ax + b

'''
import math
from fractions import Fraction

x1,y1 = (-2,3)
x2,y2 = (2,5)


if x1 == x2 and y1 == -y2 :
	print("(x3,y3) is a point at infinity")
else :
	if x1 == x2 and y1 == y2 :
		lamda = (3 * math.pow(x1,2) + a)/2*y1
	else : 
		lamda = (y2-y1)/(x2-x1)

x3 = math.pow(lamda,2) - x1 - x2
y3 = (lamda*(x1-x3)) - y1
print(x3,y3)
print("")
print(Fraction(x3),Fraction(y3))