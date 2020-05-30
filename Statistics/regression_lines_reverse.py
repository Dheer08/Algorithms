import numpy as np
import math
from scipy.stats.stats import pearsonr

#ax+by=c
#px+qy=r
A = np.array([[8,-10],[40,-18]])
B = np.array([-66,214])
X = np.linalg.solve(A,B)

mean_x = X[0]
mean_y = X[1]

print("mean_x : ",mean_x)
print("mean_y : ",mean_y)

# Equations : (x - x_mean) = bxy(y - y_mean) , (y - y_mean) = byx(x - x_mean)

# case : 1 => 8x = 10y - 66 , 18y = 40x + 214
bxy = 10/8
byx = 40/18
r = math.sqrt(bxy*byx)
print("case 1 : ",r)

# case : 2 => 10y = 8x + 66 , 40x = 18y - 214
bxy = 18/40
byx = 8/10
r = math.sqrt(bxy*byx)
print("case 2 : ",r)

# selecting r such a way that r<=1 && r>=1
# if byx and bxy are -ve then r is also -ve
# for -ve numbers math.sqrt(-ve) gives "domain error" 