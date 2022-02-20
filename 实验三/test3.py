import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.arange(0, 1, 0.1)
y = (x * x - 5 * x + 3) * np.exp(-4 * x) * np.cos(x)

plt.scatter(x, y)

for n in ['zero', 'slinear', 'quadratic']:
    f = interp1d(x, y, kind = n)
    plt.plot(x, f(x), label = n)

plt.legend(loc = "upper right")
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.title("插值曲线")

plt.show()


