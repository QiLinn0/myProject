import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

x = np.arange(1, 51, 1)
y = binom.pmf(x, 50, 0.1)

sum = 0

for i in range(9, 40):
    sum = sum + y[i]

print("概率为", sum)
