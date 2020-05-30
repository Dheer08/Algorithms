import numpy as np
from scipy import stats

data_x = np.array([1,2,3,4,5,6])
mean_1  = np.mean(data_x)

#if each observariation is associated with corresponding weight(frequency)
freq = np.array([1,2,3,4,5,6])
data_freq = data_x*freq
data_freq_sum = np.sum(data_freq)
freq_sum = np.sum(freq) 
mean_2 = data_freq_sum/freq_sum

print("mean 1 : ",mean_1)
print("mean 2 : ",mean_2)