import numpy as np
import matplotlib.pyplot as plt
import math

T = -130 + 273.15

def p(V, T, a, b):
    R = 8.314
    return (R*T)/(V-b) - a/(V**2)

b = 3.19*10**(-5)
a = 0.1382

XDataV = np.arange(b + 10**(-5), 10**(-3), 10**(-7))

XMin1 = 4 * 10 ** (-5)
XMin2 = 6 * 10 ** (-5)
while XMin2 - XMin1 >= 10**(-7):
    a = (XMin2 - XMin1) / 3
    if p(XMin1 + a, T, a, b) < p(XMin2 - a, T, a, b):
        XMin2 -= a
    else:
        XMin1 += a
Min = XMin1


Xmax1 = 0
Xmax2 = 0.0001
while Xmax2 - Xmax1 >= 10 ** (-7):
    a = (Xmax2 - Xmax1) / 3
    if p(Xmax1 + a, T, a, b) < p(Xmax2 - a, T, a, b):
        Xmax2 -= a
    else:
        Xmax1 += a
Max = Xmax1

YData = []
for i in XDataV:
    YData.append(p(i, T, a, b))
YData = np.array(YData)

plt.plot(XDataV, YData)
# plt.scatter(Max, p(Max, T, a, b))
# plt.scatter(Min, p(Min, T, a, b))

# print(Min)
print(Max)

# plt.show()
