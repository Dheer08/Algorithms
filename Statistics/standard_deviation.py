import numpy as np
from scipy import stats
import scipy
import math

# if data is not a frequency distribution
x = np.array([1,2,3,4,5])
mean = np.mean(x)
n = x.size
x_minus_mean= x-mean
x_minus_mean_square = np.square(x_minus_mean)
x_minus_mean_square_sum = np.sum(x_minus_mean_square)

standard_deviation = math.sqrt(x_minus_mean_square_sum/n)
print("standard_deviation 1 : ",standard_deviation)

# if dataset is frequency distribution
x_square = np.square(x)
f = np.array([6,16,24,25,19])
cum_freq = np.array([6,22,46,71,90])
f_x_square = f*x_square

sum_f_x_square = np.sum(f_x_square)
sum_f = np.sum(f)
mean_square = math.pow(mean,2)
standard_deviation = math.sqrt((sum_f_x_square/sum_f) - mean_square)

print("standard_deviation 2 : ",standard_deviation)