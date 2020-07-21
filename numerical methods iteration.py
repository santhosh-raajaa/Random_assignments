from math import *

x0=float(input('enter starting interval:'))
k=0



for i in range(0,100+k):
    c=x0
    x1=((2*c)+5)**(1/3)
    x0=x1
    print('x',i+1,'=',round(x1,5))
    if i==99:
        k=k+1
    if round(c,4)==round(x1,4):
        print('the root is',round(x1,4))
        print(i+1,'th iteration')
        break
    elif round(x0,4)!=round(x1,4):
        continue
