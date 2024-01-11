import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x**3+x-1
def sec_m(x0,x,tol,N):
    A=[]
    i=1
    if abs(f(x))<=tol:
        print("roots of the equation is :",x)
    elif abs(f(x0))<=tol:
        print("roots of the equation is :",x0)
    else:
        while abs(f(x0))>=tol:
            print((f(x)-f(x0)))
            A.append(x)
            if abs(f(x)-f(x0))==0:
                #print("secant method fails you may change the interval or equation has no roots ")
                break
            x1=x-((f(x)*(x-x0))/(f(x)-f(x0)))
            print(i,"iteration ",x1)
            if i>N:
                print("secant method fails you may change the interval or equation has no roots ")
                break
            x0=x
            x=x1
            i=i+1
        if i<N:
            print("roots of equation is :",x)
            X=np.linspace(-20,20,2000)
            plt.plot(X,f(X),label='function')
            plt.ylim(-10,10)
            plt.xlim(-20,20)
            plt.plot(np.array(A),0*np.array(A),'r.',markersize='5',label='iterations')
            plt.plot(x,0,'b.',markersize='8',label='root')
            plt.legend()
            plt.grid()
            plt.show()


x0=eval(input("enter the first limt :"))
x=eval(input("enter the second limt :"))
t=0.0000000
n=eval(input("enter the maximum no. of iteration :"))
sec_m(x0,x,t,n)

#3*np.exp(2*x)+x**2-3   3*np.exp(2*x)+(x)**2-5