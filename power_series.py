import numpy as np
import matplotlib.pyplot as plt
#for experimental purpose input w as experimental values of y and t as the experimental values of x
# Define the parameters for the exponential curve
a = 2  # amplitude
m1 = 2  # exponential rate
t = np.linspace(1,5,10)  # x values
w=[]
y_true = a*(t**m1)
for i in range(0,len(t)):
    y_n=y_true[i]+np.random.randint(0,5)
    w.append(y_n)
y=np.log(w)
x=np.log(t)
print('N=',len(x))
sx=sum(x)
print("sum of xi= ",sx)
sy=sum(y)
print("sum f yi= ",sy)
sxy=0
sx2=0
for i in range(0,len(x)):
    sxy=sxy+x[i]*y[i]
    sx2=sx2+x[i]*x[i]
print("sum of xiyi= ",sxy)
print("sum of xi^2= ",sx2)
m=(len(x)*sxy-sx*sy)/(len(x)*sx2-(sx)**2)
print("slop of line is :",m)
b=(sy-m*sx)/len(x)
print("y intercept of line is :",b)
def lin(x1):
    return m*x1+b
x3=np.linspace(min(x),max(x))
y2=lin(x3)
plt.subplot(2,1,1)
plt.plot(x,y,'g.',label='actual points')
plt.plot(x3,y2,'y',label='best fit line')
plt.grid()
plt.legend()
plt.xlabel("x-->")
plt.ylabel("log(y)-->")
#plt.show()
def f1(x):
    return np.exp(b)*((np.exp(x)**m))
y1=f1(x3)
print("exponential-",m,"amplitude-",np.exp(b))
plt.subplot(2,1,2)
plt.plot(x3,y1,label='best fit line')
plt.plot(x,w,'r.',label='actual points')
plt.grid()
plt.legend()
plt.xlabel("x-->")
plt.ylabel("y-->")
plt.show()