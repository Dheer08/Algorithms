import numpy as np
import math
from scipy import stats

x = np.array([14.4,7.2,27.5,53.8,38.0,15.9,4.9])
y = np.array([54,64,44,32,37,68,62])

n = x.size

rank_x = np.array([5,6,3,2,1,4,7])
rank_y = np.array([4,2,5,7,6,1,3])

d = rank_x - rank_y
d_square = np.square(d)
sum_d_square = np.sum(d_square)

print("d : ",d)
print("d_square : ",d_square)

# if there are no duplicates
coeff_numerator = 6*sum_d_square

# if there are duplicates
coeff_numerator_dup = 6*(sum_d_square+((6+24)/12))

coeff_denominator = n*(math.pow(n,2)-1)
coeff = 1-(coeff_numerator/coeff_denominator)

print("rank co-relation : ",coeff)