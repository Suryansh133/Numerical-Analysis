import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.exp(-x)*np.sin(x)


x=int(input("enter the interval :"))
X=np.linspace(-x,x,500000)
y=f(X)
Y=X*0
z=X*0
print(X)
print(y)
plt.plot(X,Y)
plt.plot(X,y)
plt.plot(z,X)
plt.ylim(-20,20)
plt.xlim(-10,10)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

#5*x**5+4*(x**2)-4*(x)+3