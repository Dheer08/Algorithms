import math

def gcd_lcd(x,y):
	gcd = math.gcd(x,y)
	lcd = (x*y)//gcd
	return gcd,lcd

a = 91
b = 48
results = gcd_lcd(a,b)
print(f"gcd : {results[0]},lcd : {results[1]}")