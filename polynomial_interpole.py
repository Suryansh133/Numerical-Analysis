import numpy as np
import matplotlib.pyplot as plot
x = [1, 3, 5, 7, 8, 9, 10, 12, 13]
y = [50, -30, -20, 20, 5, 1, 30, 80, -10]
n = len(x) - 1
prange = np.linspace(min(x), max(x), 500)
plot.plot(x, y,'r.')
def f(o):
    sum = 0
    for i in range(n + 1):
        prod = y[i]
        for j in range(n + 1):
            if i != j:
                y1= prod * (o - x[j]) / (x[i] - x[j])
                y1=y1*y1
        sum = sum + y1
    return sum
plot.plot(prange, f(prange))
plot.show()