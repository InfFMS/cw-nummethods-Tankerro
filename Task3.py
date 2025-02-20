import numpy as np
import matplotlib.pyplot as plt

T = -130 + 273.15
b = 3.19*10**(-5)
a = 0.1382


def find_curve_len(x, y):
    sum = 0
    i = 0
    j = 0
    while i < len(x)-1 and j < len(y)-1:
        sum += ((x[i+1]-x[i])**2 + (y[j+1]-y[j])**2)**(1/2)
        i += 1
        j += 1
    return sum

def p(V, T, a, b):
    R = 8.314
    return (R*T)/(V-b) - a/(V**2)

Max = 0.0001361469746634903
Min = 0.00007190654057018651

XDataV = np.arange(Min, Max, 10**(-8))
YData = []
for i in XDataV:
    YData.append(p(i, T, a, b))
YData = np.array(YData)

print(f"Length {find_curve_len(XDataV, YData)}")

plt.plot(XDataV, YData)
plt.show()