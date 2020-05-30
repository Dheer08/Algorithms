import numpy as np
from scipy.stats.stats import pearsonr
import math

x = np.array([87,84,88,102,101,84,72,84,83,98,97,100])
y = np.array([88,79,83,97,96,90,82,84,88,100,91,102])

values = pearsonr(x,y)
r = values[0]

sigma_y = np.std(y,dtype=np.float32)
sigma_x = np.std(x,dtype=np.float32)

bxy = r * (sigma_x/sigma_y)
byx = r * (sigma_y/sigma_x)

print(bxy)
print(byx)