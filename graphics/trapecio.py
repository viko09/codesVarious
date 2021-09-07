import numpy as np


def f(x):
    return np.exp(-1*x ** 2)


a = 0
b = 1

N = 10
x = np.linspace(a, b, N)
dx = (b-a)/(N-1)


I = 0
for i in range(N-1):
    T = (x[i+1] - x[i]) * (f(x[i + 1]) + f(x[i])) / 2
    I = I+T

print(I)