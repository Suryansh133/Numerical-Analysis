import matplotlib.pyplot as plt
import numpy as np
R=eval(input("enter the value of resistance :"))
t=eval(input("enter the value of time period :"))
C=eval(input("enter the value of Capacitance :"))
h=eval(input("enter the value step size :"))
def f(x,y1,vs):
    return (vs-y1)/R*C
def eul():
    X=[]
    Y=[]
    i = 0
    vs = eval(input("enter the value of applied voltage :"))
    vi = eval(input("enter the value of initiall voltage"))
    while i<t:
        y=vi+f(t,vi,vs)*h
        X.append(i)
        Y.append(vi)
        vi=y
        i=i+h
    print(Y)
    plt.plot(X,Y,label="euler's method")
eul()
#modified euler's
def eulm():
    X = []
    Y = []
    i = 0
    vs = eval(input("enter the value of applied voltage :"))
    vi = eval(input("enter the value of initiall voltage"))
    while i < t:
        yeu = vi+f(t,vi,vs)*h/2
        y=vi+f(t,yeu,vs)*h
        X.append(i)
        Y.append(vi)
        vi = y
        i = i + h
    print(Y)
    plt.plot(X, Y, label="modified euler's method")
eulm()
##rk2
def rk2():
    X = []
    Y = []
    i = 0
    vs = eval(input("enter the value of applied voltage :"))
    vi = eval(input("enter the value of initiall voltage"))
    while i < t:
        k1=f(t,vi,vs)
        k2=f(t+h,vi+(k1*h),vs)
        y=vi+((k1+k2)/2)*h
        X.append(i)
        Y.append(vi)
        vi=y
        i = i + h
    print(Y)
    plt.plot(X, Y, label="rk2 method")
rk2()
##rk4
def rk4():
    X = []
    Y = []
    i = 0
    vs = eval(input("enter the value of applied voltage :"))
    vi = eval(input("enter the value of initiall voltage"))
    while i < t:
        k1=f(t,vi,vs)
        k2=f(t+h/2,vi+(k1/2)*h,vs)
        k3=f(t+h/2,vi+(k2/2)*h,vs)
        k4=f(t+h,vi+(k3*h),vs)
        y=vi+1/6*(k1+2*k2+2*k3+k4)*h
        X.append(i)
        Y.append(vi)
        vi = y
        i = i + h
    print(Y)
    plt.plot(X, Y, label="rk4 method")
rk4()
plt.legend()
plt.show()