import numpy as np
import matplotlib.pyplot as plt
def nut_cool():
    To = eval(input('enter the initial temprature :'))
    Ts = eval(input('enter the surrounding temprature :'))
    k=eval(input('enter the cooling constant in min^-1 :'))
    s = int(input("enter the time limit :"))
    x2 = int(input("enter the time which have to find Temprature :"))
    t = np.arange(0, s)

    def Temp(Ts, To, k, t):
        return Ts + (To - Ts) * np.exp(-k * t)
    ta = Temp(Ts, To, k, t)
    t1 = Temp(Ts, To, k, x2)
    print('actual temprature at t', ta)
    # euler's method
    T = []
    Y = []
    ts = To
    for i in range(0, s):
        if i == x2:
            f = ts
            d = i
        tr = ts - k * (ts - Ts)
        Y.append(ts)
        T.append(i)
        ts = tr
    print('temprature acc. to euler method :', Y)
    # modified euler's method
    T1 = []
    Y1 = []
    ts1 = To
    for i1 in range(0, s):
        if i1 == x2:
            f1 = ts1
            d1 = i1
        teu = ts1 - k * (ts1 - Ts) * 1 / 2
        tr1 = ts1 - k * (teu - Ts) * 1
        Y1.append(ts1)
        T1.append(i1)
        ts1 = tr1
    plt.plot(t, ta, label=('actual temp. for k',k))
    print('temprature acc. to modified euler method',Y1)
    plt.plot(T,Y,label=("euler's method for k=",k))
    plt.plot(T1, Y1, label=("modified euler's method for k=",))

nut_cool()
nut_cool()
nut_cool()
plt.xlim(0,30)
plt.ylabel("T(t)")
plt.xlabel('t(min)')
plt.legend()
plt.grid()
plt.show()