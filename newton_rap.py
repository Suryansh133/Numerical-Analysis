import matplotlib.pyplot as plt
import numpy as np
def f(x):
    # x**2-4
    return x**2-1
def fd(x):
    return 2*x
def new_rap(x0,tol,n):
    a=[]
    # x=x0-f(x0)/fd(x0)
    x1=np.linspace(-50,50,3000)
    i=1
    while abs(f(x0))>tol:
        if fd(x0)==0:
            print("newton raphson fails, you may change the assumed roots or  equation has no roots")
            break
        x = x0-f(x0)/fd(x0)
        list.append(a,x0)
        print(i,"iteration is :",x)
        if i>n:
            print("newton raphson fails, you may change the assumed roots or  equation has no roots")
            break
        x0=x
        i=i+1
    print('root of the equation is',x)
    plt.plot(x1,f(x1),label='function')
    plt.plot(x,0,marker='*',label='root',markersize='8',color='blue')
    plt.ylabel('f(x)')
    plt.xlabel("x")
    plt.plot(np.array(a),0*np.array(a),'ro',markersize='5',label='iteration')
    plt.ylim(-10,10)
    plt.xlim(-10,10)
    plt.grid()
    plt.legend()
    plt.show()

    print("root of equation is :",x0)

a=eval(input("enter the assumed root :"))
t=0.000000001  #eval(input("enter the tollerence :"))
n=int(input('enter the max no of iteration :'))
new_rap(a,t,n)