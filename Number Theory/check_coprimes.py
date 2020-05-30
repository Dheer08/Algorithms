import math

a = 2
b = 4
gcd  = math.gcd(a,b)

if gcd == 1 :
	print(a,",",b,"are co-primes")
else : 
	print("gcd : ",gcd)
	print(a,",",b,"are not co-primes")