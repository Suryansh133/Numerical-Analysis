import numpy as np
import matplotlib.pyplot as plt
y=[0.44,2.162,3.572,6.002,7.896,12.673,14.364,19.184,21.068]
x=[0,1,2,3,4,6,7,9,10]
print('N=',len(x))
sx=sum  (x)
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
plt.plot(x,y,'g.',label='actual points')
plt.plot(x3,y2,'y',label='best fit line')
plt.grid()
plt.legend()
plt.xlabel("x-->")
plt.ylabel("y-->")
plt.show()