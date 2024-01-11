"""suryansh roll no 086"""
import numpy as np
def f(x):
    return np.tan(x)-x
def sec_m(x1,x2,tol,N):
    i=1
    if abs(f(x1))<=tol:
        print("roots of the equation is :",x1)
    while abs(f(x2))>=tol:
        if abs(f(x2)-f(x1))==0:
            break
        x3=x2-((f(x2)*(x2-x1))/(f(x2)-f(x1)))
        print(i,"iteration is :",x3)
        if i>N:
            print("secant method fails you may change the interval or equation has no roots ")
            break
        x1=x2
        x2=x3
        i=i+1
    print("root of the equation is :",x2)
x0=eval(input("enter the first limt :"))
x=eval(input("enter the second limt :"))
t=0.0000000
n=eval(input("enter the maximum no. of iteration :"))
sec_m(x0,x,t,n)
