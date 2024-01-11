import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return x**3+x-1
a1=eval(input("enter the initial value of intervel :"))
b1=eval(input("enter the final value of intervell :"))
t=eval(input("enter the tollrence"))
def bisec(a,b,tol):
    i = 1
    X = []
    while abs(b - a) >= tol:
        if f(a) * f(b) > 0:
            print("change the intervall or roots may not exist")
            break
        c = (a + b) / 2
        X.append(c)
        print(i, "iteration is ", c)
        if abs(f(c)) <= tol:
            print("roots of the equation is :", c)
            break
        if f(a) * f(c) < 0:
            b = c
        elif f(b) * f(c) < 0:
            a = c
        i = i + 1
    plt.plot(np.array(X), (0 * np.array(X)), '.', label='iterations')
    plt.plot(c, 0, '*', label='root')
x1=np.linspace(a1,b1,1000)
plt.plot(x1,f(x1),label='function')
bisec(a1,b1,t)
plt.grid()
plt.legend()
plt.show()