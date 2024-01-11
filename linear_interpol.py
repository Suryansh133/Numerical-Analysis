import numpy as np
import matplotlib.pyplot as plt
xo=eval(input("enter the initial value of independent variable :"))
yo=eval(input("enter the initial value of function :"))
xf=eval(input("enter the final value of independent variable :"))
yf=eval(input("enter the final value of function :"))
n=10
h=(xf-xo)/n
y=[]
x=[]
for i in range(0,n):
    y.append(yo)
    x.append(xo)
    y1=yo+h*((yf-yo)/(xf-xo))
    yo=y1
    xo=xo+h
plt.plot(x,y)
plt.show()
print(x,y)