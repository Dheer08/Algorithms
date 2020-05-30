import numpy as np
from scipy import stats
import math

x = np.array([5,15,25,35,45])
x_square = np.square(x)

f = np.array([6,16,24,25,19])
cum_freq = np.array([6,22,46,71,90])
f_x_square = f*x_square

# mean
mean = np.average(x,weights=f)

# mode for now find manually
l = 30
f0 = 10
f1 = 12
f2 = 8
c = 10
mode  = l + ((f1 - f0)/(2*f1 - c*f0 + f2))*c
mode  = 31.4

# standard deviation
sum_f_x_square = np.sum(f_x_square)
sum_f = np.sum(f)
mean_square = math.pow(mean,2)
standard_deviation = math.sqrt((sum_f_x_square/sum_f) - mean_square)

print("mean : ",mean)
print("mode : ",mode)
print("standard_deviation : ",standard_deviation)

coeff = (mean - mode)/standard_deviation

print("Coefficent : ",coeff)