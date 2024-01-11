import numpy as np
import math
from sympy import *
N = 5
def lag_weights_roots(n):
    x = Symbol("x")
    roots = Poly(laguerre(n, x)).all_roots()
    x_i = [rt.evalf(20) for rt in roots]
    w_i = [(rt / ((n + 1) * laguerre(n + 1, rt)) ** 2).evalf(20) for rt in roots]
    return x_i, w_i
print(lag_weights_roots(N))
xi, wi = lag_weights_roots(N)
def f1(x):
    return((math.exp(x))/(1+(x**6)))
sum = 0
def f2(x):
    return math.sin(x)/x
for i in range(N):
    sum = sum + wi[i]*f1(xi[i])
print("For n =", N)
print("Integral =", sum)
print("Error =", 100*abs(sum-np.pi/3)/(np.pi/3))