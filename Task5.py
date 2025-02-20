import numpy as np
import matplotlib.pyplot as plt


P_up = 3664186.998

V1 = 0.0000615
V2 = 0.00010046875
Vg = 0.00019488281250000001

X1 = np.arange(V1, V2, 0.000001)
X2 = np.arange(V2, Vg, 0.000001)


def p(V):
    T = -130 + 273.15
    b = 3.19 * 10 ** (-5)
    a = 0.1382
    R = 8.314
    return (R*T)/(V-b) - a/(V**2)

def calc(array, func):
    x = array[0]
    y1 = func(x)
    sum = 0
    while x < array[len(array)-1]:
        x += 0.001
        y2 = func(x)
        sum += 0.5 * (y1 + y2) * 0.001
        y1 = y2
    return sum

Integral1 = calc(X1, p)
Integral2 = calc(X2, p)

if Integral1 - Integral2 <= 100:
    print("УРААААААА!!!! Правило Максвелла выполняется!!! Тогда отметим эту победу: https://www.youtube.com/watch?v=dQw4w9WgXcQ")
else:
    print("Блин((( не выполняется, посмотрим тогда видео: https://www.youtube.com/watch?v=dQw4w9WgXcQ")