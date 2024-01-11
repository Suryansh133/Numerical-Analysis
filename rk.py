import numpy as np
import matplotlib.pyplot as plt
##decay problem by using rk method
#4th order rk method
def rk():
    def f(x1, y, K1):
        return -K1 * (y)
    yo = eval(input("enter the initial value of nuclei :"))
    K = eval(input("enter the value of decay constant"))
    s = eval(input("enter the time period: "))
    def rk4(y1, s1):
        X1 = []
        Y1 = []
        h1 = eval(input("enter the step size: "))
        x1 = 0
        while x1 < s1:
            k1 = f(x1, y1, K)
            k2 = f((x1+h1/2), (y1+(k1/2)*h1), K)
            k3 = f((x1+h1/2), (y1+(k2/2)*h1), K)
            k4 = f((x1+h1), (y1+k3*h1), K)
            y2 = y1 + h1*(k1+2*k2+2*k3+k4)/6
            X1.append(x1)
            Y1.append(y1)
            y1 = y2
            x1 = x1 + h1
        print("rh4 radio decay", Y1)
        plt.plot(X1, Y1, label=('RK4 for k=', K))
    ##second order rk method
    def rk2(y1, s1):
        X = []
        Y = []
        h = eval(input("enter the step size: "))
        x = 0
        while x < s:
            k11 = f(x, y1, K)
            k21 = f((x+h), (y1+k11*h),K)
            y21 = y1 + h * (k11 + k21) / 2
            X.append(x)
            Y.append(y1)
            y1 = y21
            x = x + h
        print(Y)

    rk4(yo, s)
    rk2(yo, s)

rk()
rk()
rk()
plt.legend()
plt.grid()
plt.show()
