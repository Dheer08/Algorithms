import numpy as np
from scipy.stats.stats import pearsonr

x = np.array([25,35,10,40,85,75,60,45,50])
y = np.array([63,68,72,62,65,46,51,60,55])


print(pearsonr(x,y))
