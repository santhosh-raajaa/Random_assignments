print('#READ BEFORE USE(PORUPU THURAPPU!!!!)')

print('#THE DATAS SHOULD BE GIVEN AS AN INPUT, ONLY AFTER CONVERTED TO THE SPECIFIED UNITS')
print('#IMPROPER INPUT MAY RESULT IN INCORRECT OUTPUT')
print('#IN ANY CURCUMSTANCES,UNDER THESE CONDITIONS,THE DEVELOPER IS NOT RESPONSIBLE FOR THE INCORRECT OUTPUT')
print('#THE PROGRAM IS DEVELOPED UNDER THE ASSUMPTION THAT PRESSURE IS CONSTANT IN THE GIVEN SYSTEM')
print('#FLUIDS OF DEFINITE MASS AT DEFINITE TEMPURATURE IS CONSIDERED TO BE A "SYSTEM",n NUMBER OF SYSYEMS CAN BE CONSIDERED ACCORDINGLY')






import math
from math import log,e
tol_AE=0
T0=float(input('enter temperature of surrounding in Kelvin:'))
Cp=float(input('enter specific heat capacity of respective fluid in (kJ/kgK):'))
list_of_masses=list()
list_of_temp=list()
list_of_pdt=list()
number_of_systems=int(input("enter the number of systems involved:"))
for i in range(0,number_of_systems):
    print('enter the respective values of system',i+1)
    m=float(input('enter mass of fluid in kg:'))
    T=float(input('enter temperature of fluid in Kelvin:'))
    pdt=m*T
    list_of_masses.append(float(m))
    list_of_temp.append(float(T))
    list_of_pdt.append(float(pdt))
    Av_En=m*Cp*((T-T0-(T0* log(T/T0 ,e))))
    tol_AE=tol_AE+Av_En
    
print('mass of fluid in respective',number_of_systems,'systems:',list_of_masses)
print('temperature of fluid in respective',number_of_systems,'systems:',list_of_temp)
print('total available energy before mixing:',tol_AE,'J')

t=0
s=0
for ele in range(0,len(list_of_pdt)):
    t=t+list_of_pdt[ele]
for ele in range(0,len(list_of_masses)):
    s=s+list_of_masses[ele]

Tf=t/s
print('mean temperature of fluid after mixing:',Tf,'K')

tol_AE_afmix=s*Cp*((Tf-T0-(T0* log(Tf/T0 ,e))))
print('total available energy after mixing:',tol_AE_afmix,'kJ')

de_AE=tol_AE-tol_AE_afmix
print('the decrease in available energy after mixing:',de_AE,'kJ')



    
