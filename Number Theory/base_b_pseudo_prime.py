import math
import sympy

b = 8
n = 21
temp = math.pow(b,n-1)
mod = temp%n

'''
if n is prime and math.pow(b,n-1) = 1 mod n then n is base b probable prime
if n is composite and math.pow(b,n-1) = 1 mode n then n is base b pseudo prime
'''

if sympy.isprime(n) and mod == 1 :
	print(f"{n} is a base {b} probable prime")
elif sympy.isprime(n) == False and mod == 1 : 
	print(f"{n} is a base {b} pseudo prime")

