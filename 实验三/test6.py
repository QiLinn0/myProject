from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def fun(y, x):
    return (np.exp(x) - y) / x

x = np.arange(1, 6, 0.1)
y = odeint(fun, 2, x)

plt.plot(x,y)
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.title("解函数的曲线")
plt.show()