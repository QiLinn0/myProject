import numpy as np
from scipy.integrate import tplquad

val3, err = tplquad(lambda z, y, x: y * np.sin(x) * np.exp(x) + z * np.cos(x) * x * x,
               -0.5, 1,
               0, 0.5,
               -0.5 * np.pi, np.pi)

print("三重积分的值是：", val3)
