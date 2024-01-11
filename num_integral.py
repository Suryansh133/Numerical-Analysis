#Numerical integration
#Trapizoidal method
import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return (2000*np.log(140000/(140000-2100*t))-9.8*t)
a=eval(input("enter the initial value of interval :"))
b=eval(input("enter the final value of interval :"))
n=eval(input("enter the number of segament :"))
i=1
X=[]
Y=[]
while i<=n:
    h=abs(b-a)/i
    A=np.arange(a,b,h)
    I=0
    for j in A:
        I=I+(h*((f(j)+f(j+h))))/2
    print('integral for n=',i,I)
    e = (abs(I -11061)/11061)*100
    X.append(i)
    Y.append(e)
    print('for n=',i,'-',e)
    i = i + 1
x = np.linspace(a,b+h,1000)
plt.subplot(2, 1, 1)
plt.plot(x, f(x),label='actual curve')
plt.plot(A,f(A),label='assumed curve')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(X, Y)
plt.ylabel("error")
plt.xlabel("no. of segament")
plt.grid()
plt.show()