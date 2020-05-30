import numpy as np
from scipy.stats.stats import pearsonr
import math

x = np.array([87,84,88,102,101,84,72,84,83,98,97,100])
y = np.array([88,79,83,97,96,90,82,84,88,100,91,102])

r = pearsonr(x,y)

print(r[0])