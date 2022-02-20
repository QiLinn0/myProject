import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 13, 1)
y = [989, 1012, 1022, 976, 1041, 1025, 991, 1098, 1019, 910, 1021, 1015]

z1 = np.polyfit(x, y, 1)
p1 = np.poly1d(z1)
y1 = p1(x)
plt.plot(x, y1, color = "green", linestyle = "-", label = 'a fit')
plt.legend(loc = "upper right")

z2 = np.polyfit(x, y, 2)
p2 = np.poly1d(z2)
y2 = p2(x)
plt.plot(x, y2, color = "blue", linestyle = "--", label = 'quadratic fit')
plt.legend(loc = "upper right")

z3 = np.polyfit(x, y, 3)
p3 = np.poly1d(z3)
y3 = p3(x)
plt.plot(x, y3, color = "red", linestyle = ":", label = 'cubic fit')
plt.legend(loc = "upper right")

plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.title("拟合曲线")

plt.show()