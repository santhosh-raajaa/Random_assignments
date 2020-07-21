print('1)force exerted by jet on the stationary plate ,perpendicular to jet')
print('2)force exerted by jet on the stationary plate inclined to jet')
print('3)force exerted by jet on the stationary curved plate')
print('   a)jet passing at centre of symmentrical plate')
print('   b)jet passing tangentially at symmentrical plate')
print('   c)jet passing tangentially at unsymmentrical plate')
print()
print('4)force exerted by jet on moving plate perpendicular to jet')
print('5)force exerted by jet on moving plat inclined to jet')
print('6)force exerted by jet on moving curved plate ,when jet hitting at centre')
print()
print('(NOTE:ALL INPUTS SHOULD BE GIVEN IN SI UNITS)')

sum_model=str(input('enter the model type:'))
import math
from math import *


if sum_model=='1':
    den=float(input('enter density of jet:'))
    d=float(input('enter diameter of jet:'))
    v=float(input('enter velocity of jet:'))
    Fx=(den*pi*d*d*v*v)/4
    print('Fx=',Fx,'N')
    print('work done per second =0')
elif sum_model=='2':
    den=float(input('enter density of jet:'))
    d=float(input('enter diameter of jet:'))
    v=float(input('enter velocity of jet:'))
    deg=float(input('enter the inclined angle:'))
    Fn=den*(pi*d*d/4)*v*v*(sin(radians(deg)))
    Fx=Fn*sin(radians(deg))
    Fy=Fn*cos(radians(deg))
    print('Fn=',Fn,'N')
    print('Fx=',Fx,'N')
    print('Fy=',Fy,'N')
    print('work done per second =0')
elif sum_model=="3":
    sub=str(input('enter the sub-model:'))
    if sub=='a':
        den=float(input('enter density of jet:'))
        d=float(input('enter diameter of jet:'))
        v=float(input('enter velocity of jet:'))
        deg=float(input('enter the outlet velocity angle:'))
        Fx=den*(pi*d*d/4)*(v**2)*(1+cos(radians(deg)))
        Fy=den*(pi*d*d/4)*(v**2)*(-sin(radians(deg)))
        print('Fx=',Fx,'N')
        print('Fy=',Fy,'N')
        print('work done per second =0')
    elif sub=='b':
        den=float(input('enter density of jet:'))
        d=float(input('enter diameter of jet:'))
        v=float(input('enter velocity of jet:'))
        deg=float(input('enter inlet/outlet velocity angle:'))
        Fx=2*den*(pi*d*d/4)*(v**2)*(cos(radians(deg)))
        Fy=0
        print('Fx=',Fx,'N')
        print('Fy=',Fy,'N')
        print('work done per second =0')
    elif sub=='c':
        den=float(input('enter density of jet:'))
        d=float(input('enter diameter of jet:'))
        v=float(input('enter velocity of jet:'))
        deg1=float(input('enter the inlet velocity angle:'))
        deg2=float(input('enter the outlet velocity angle:'))
        Fx=den*(pi*d*d/4)*v(v*cos(radians(deg1))-v*cos(radians(deg2)))
        Fy=den*(pi*d*d/4)*v(v*sin(radians(deg1))-v*sin(radians(deg2)))
        print('Fx=',Fx,'N')
        print('Fy=',Fy,'N')
        print('work done per second =0')
elif sum_model=='4':
    den=float(input('enter density of jet:'))
    d=float(input('enter diameter of jet:'))
    v=float(input('enter velocity of jet:'))
    u=float(input('enter velocity if vane:'))
    Fx=den*(pi*d*d/4)*(v-u)**2
    print('Fx=',Fx,'N')
    wd=Fx*u
    print('work done per second=',wd,'w')
elif sum_model=='5':
    den=float(input('enter density of jet:'))
    d=float(input('enter diameter of jet:'))
    v=float(input('enter velocity of jet:'))
    u=float(input('enter velocity if vane:'))
    deg=float(input('enter the angle of inclination of plate:'))
    Fn=den*(pi*d*d/4)*((v-u)**2)*sin(radians(deg))
    Fx=Fn*sin(radians(deg))
    Fy=Fn*cos(radians(deg))
    print('Fn=',Fn,'N')
    print('Fx=',Fx,'N')
    print('Fy=',Fy,'N')
    wd=Fx*u
    print('work done per second=',wd,'w')
elif sum_model=='6':
    den=float(input('enter density of jet:'))
    d=float(input('enter diameter of jet:'))
    v=float(input('enter velocity of jet:'))
    u=float(input('enter velocity if vane:'))
    deg=float(input('enter the angle at which jet leaves the plate:'))
    Fx=den*(pi*d*d/4)*((v-u)**2)*(1+cos(radians(deg)))
    Fy=den*(pi*d*d/4)*((v-u)**2)*(-sin(radians(deg)))
    wd=den*(pi*d*d/4)*((v-u)**2)*u*(1+cos(radians(deg)))
    print('Fx=',Fx,'N')
    print('Fy=',Fy,'N')
    print('work done per second=',wd,'w')
    
    
    
        

        
        





        
        
    
    


    
    
