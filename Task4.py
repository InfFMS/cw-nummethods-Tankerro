import numpy as np
import matplotlib.pyplot as plt

P_up = 3664186.998


def solve(A, B, f, eps):
    while B - A >= 2*eps:
        x = (B + A) / 2
        if f(A, 1)*f(x, 1) <= 0:
           B = x
        else:
            A = x
    print(x)
    return x

T = -130 + 273.15
b = 3.19*10**(-5)
a = 0.1382

def p(V, T, a, b, P_up):
    R = 8.314
    return (R*T)/(V-b) - a/(V**2) - P_up

XDataV = np.arange(b + 10**(-5), 10**(-3), 10**(-7))
YData = []
for i in XDataV:
    YData.append(p(i, T, a, b, P_up))
YData = np.array(YData)




def f(V, P_up):
    P_up = 3664186.998
    return p(V, T, a,  b, P_up)

s1 =solve(0.00005, 0.000075, f, 10**(-7))
s2 = solve(0.00009, 0.00011, f, 10**(-7))
s3 = solve(0.00018, 0.00021, f, 10**(-7))
plt.scatter(s1, [p(s1, T, a,  b, P_up)])
plt.scatter(s2, [p(s2, T, a,  b, P_up)])
plt.scatter(s3, [p(s3, T, a,  b, P_up)])
plt.plot(XDataV, np.array([0]*len(XDataV)))
plt.plot(XDataV, YData)
plt.show()