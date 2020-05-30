'''
If a and b  are two integers then there exists x and y such that ax + by = gcd(x,y)

'''

def extended_euclids_algo(a,b):
	x,y,u,v = 0,1,1,0
	while a != 0 :
		q,r = b//a,b%a
		m,n = x-u*q,y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd,x,y

a = 111
b = 24
results = extended_euclids_algo(a,b)
print(f"gcd : {results[0]} , x : {results[1]} , y : {results[2]}")
print("")
print(f"{a} ({results[1]}) + {b} ({results[2]}) = {results[0]}")