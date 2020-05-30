import numpy as np
from scipy import stats
import math

x = np.array([25,35,10,40,85,75,60,45,50])
y = np.array([63,68,72,62,65,46,51,60,55])
n = x.size

mean_x = np.mean(x)
mean_y = np.mean(y)
print("mean x : ",mean_x)
print("mean y : ",mean_y)

x_i= x - mean_x
y_i = y - mean_y
print("\nxi : ",x_i)
print("yi : ",y_i)

x_i_square = np.square(x_i)
y_i_square = np.square(y_i)
xi_yi = x_i * y_i
print("\nxi**2 : ",x_i_square)
print("yi**2 : ",y_i_square)
print("xi*yi : ",xi_yi)

sum_x_i = np.sum(x_i)
sum_y_i = np.sum(y_i)
sum_xi_square = np.sum(x_i_square)
sum_yi_square = np.sum(y_i_square)
sum_xi_yi = np.sum(xi_yi)

print("\nsum_x_i : ",sum_x_i)
print("sum_y_i : ",sum_y_i)
print("sum_xi_square : ",sum_xi_square)
print("sum_yi_square : ",sum_yi_square)
print("sum_xi_yi : ",sum_xi_yi)

coeff_numerator  = ((n*sum_xi_yi) - (sum_x_i*sum_y_i))
coeff_denominator_1 = math.sqrt((n*sum_xi_square) - math.pow(sum_x_i,2))
coeff_denominator_2 = math.sqrt((n*sum_yi_square) - math.pow(sum_y_i,2))

coeff = coeff_numerator/(coeff_denominator_1*coeff_denominator_2)
print("\n coefficent of corelation : ",coeff)