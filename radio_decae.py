import numpy as np
import matplotlib.pyplot as plt
def rad():
    No = eval(input('enter the initial nuclei :'))
    s = int(input("enter the time limit :"))
    k = eval(input('enter the decay constant :'))
    x2 = int(input("enter the time which have to find no of nuclei :"))

    def decay(n, t):
        return n * np.exp(-k * t)

    def plo_d(N1, x3, s1):
        y2 = decay(N1, x3)
        x = np.arange(0, s1)
        y = decay(No, x)
        plt.plot(x, y, label=('nuclei at give time t for k=',k))
        print("actual nuclei",y)

    # euler's method
    def Neu(y1):
        x = 0
        X = []
        Y = []
        while x < s:
            y = y1 - k * y1 * 1
            X.append(x)
            Y.append(y1)
            if x == x2:
                Y3 = y1
                x3 = x
            y1 = y
            x = x + 1
        plt.plot(X, Y, label=('nuclei acc. to euler method k=',k))
        print("Nuclei Acc. to euler's method",Y)

    # modified euler's method
    def Mneu(y2):
        x1 = 0
        X1 = []
        Y1 = []
        while x1 < s:
            yeu = y2 - (k * y2) * 1 / 2
            y3 = y2 - (k * yeu) * 1
            X1.append(x1)
            Y1.append(y2)
            if x1 == x2:
                y4 = y2
                x4 = x1
            y2 = y3
            x1 = x1 + 1
        plt.plot(X1, Y1, label=('nuclei decay modified euler method for k=',k))
        print("Nuclei acc. to modified euler's method",Y1)

    plo_d(No, x2, s)
    Neu(No)
    Mneu(No)
rad()
rad()
rad()
plt.grid()
plt.legend()
plt.show()