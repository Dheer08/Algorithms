import numpy as np
from scipy import stats

# mode = 3*median - 2*mean

data = np.array([1,2,3,4,3])
mode  = stats.mode(data)

print("mode 1 : ",mode)

# if data is frequency distributed
l = 30
f0 = 10
f1 = 12
f2 = 8
c = 10

mode  = l + ((f1 - f0)/(2*f1 - c*f0 + f2))*c

print("mode 2 : ",mode)
