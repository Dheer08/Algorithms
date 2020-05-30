'''
Let n be a +ve integer and a be a integer such that gcd(a,n) = 1 then order of modulo n is the smallest integer r such that math.pow(a,r) = 1 mod n

'''
import math
import copy

n = 11
a = 4
a_temp = copy.deepcopy(a)
gcd = math.gcd(a,n)
print(f"gcd({a},{n}) = {gcd}\n")

r = a%n
i = 1
while r != 1 :
	temp = math.pow(a_temp,i)
	#print(temp)
	r = temp%n
	print(f"math.pow({a_temp},{i}) = {r} mod {n}")
	i = i + 1

print(f"\norder({a},{n}) = {i-1}")
	


