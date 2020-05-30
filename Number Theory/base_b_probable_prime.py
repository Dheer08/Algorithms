import math

b = 8
n = 9 
temp = math.pow(b,n-1)
mod = temp%n

if mod == 1 :
	print(f"{n} is a base {b} probable prime")
else : 
	print(f"{n} is not a base {b} probable prime")