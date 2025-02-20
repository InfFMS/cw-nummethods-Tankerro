import numpy as np
import matplotlib.pyplot as plt
import math

X3, axs = plt.subplots(1, 5, figsize=(10, 4))
T = [-140 + 273.15, -130 + 273.15, -120 + 273.15, -110 + 273.15, -100 + 273.15, ]

def p(V, T, a, b):
    R = 8.314
    return (R*T)/(V-b) - a/(V**2)

b = 3.19*10**(-5)
a = 0.1382


XDataV = np.arange(b + 10**(-5), 10**(-3), 10**(-7))

YData1 = []
for i in XDataV:
    YData1.append(p(i, T[0], a, b))
YData1 = np.array(YData1)

YData2 = []
for i in XDataV:
    YData2.append(p(i, T[1], a, b))
YData2 = np.array(YData2)

YData3 = []
for i in XDataV:
    YData3.append(p(i, T[2], a, b))
YData3 = np.array(YData3)

YData4 = []
for i in XDataV:
    YData4.append(p(i, T[3], a, b))
YData4 = np.array(YData4)

YData5 = []
for i in XDataV:
    YData5.append(p(i, T[4], a, b))
YData5 = np.array(YData5)

axs[0].plot(XDataV, YData1)
axs[1].plot(XDataV, YData2)
axs[2].plot(XDataV, YData3)
axs[3].plot(XDataV, YData4, "red")
axs[4].plot(XDataV, YData5, "red")

plt.show()
