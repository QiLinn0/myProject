import numpy as np
from scipy.stats import norm

x = np.random.randn(12) + 1000

x_mean, x_std = norm.fit(x)

print("正态分布的均值的最大似然估计值：", x_mean)
print("正态分布的方差的最大似然估计值：", x_std)
