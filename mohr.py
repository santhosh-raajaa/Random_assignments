from turtle import *
from math import *

t=float(input('enter shear stress:'))
s1=float(input('enter horizontal normal stress:'))
s2=float(input('enter vertical normal stress:'))
o=str(input('type "y" to enter angle from normal plane; type "n" to enter angle from principal plane:'))
s3=(s1+s2)/2
ang=degrees(atan((t)/(s1-s3)))

if o=='y':
    o=float(input('enter the angle of plane inclined:'))
elif o=='n':
    o=float(input('enter the angle from PRINCIPAL PLANE:' ))
    h=(2*o)-ang
    o=h/2

div=1
o1=2*o
s3=(s1+s2)/2


R=((((s1-s2)/2)**2)+t**2)**0.5   #real values
val=R
m=(s1+s2)/2
ang=degrees(atan((t)/(s1-s3)))
'''if ang<0:
    o1=-o1'''

if (t**2)**0.5>(s1**2)**0.5 and (t**2)**0.5>(s2**2)**0.5:
    
    while (t**2)**0.5>10:
        div=div*10
        t=t/10
        s1=s1/10
        s2=s2/10
elif(s1**2)**0.5 >(t**2)**0.5 and (s1**2)**0.5 >(s2**2)**0.5:
     while (s1**2)**0.5>10:
        div=div*10
        t=t/10
        s1=s1/10
        s2=s2/10
else:
     while (s2**2)**0.5>10:
        div=div*10
        t=t/10
        s1=s1/10
        s2=s2/10


#scale values
t=t*50
s1=s1*50
s2=s2*50

R1=(((((s1-s2)/2)**2)+t**2)**0.5)
g=R1
s3=(s1+s2)/2

def coordinate(x,y):
    print(x,y)
onscreenclick(coordinate,1)
listen()

a=Screen();a.bgcolor('black')
clear()
a.title("mohr's circle")
a.screensize(2000,2000)

r1=Turtle();r1.color('red');r1.speed('fastest')
r2=Turtle();r2.color('red');r2.speed('fastest')
r3=Turtle();r3.color('blue');r3.speed('fastest')
r4=Turtle();r4.color('blue');r4.speed('fastest')
r5=Turtle();r5.color('blue');r5.speed('fastest')
r6=Turtle();r6.color('green');r6.speed('fastest')
r7=Turtle();r7.color('green');r7.speed('fastest')
r8=Turtle();r8.color('white');r8.speed('fastest')
r9=Turtle();r9.color('white');r9.speed('fastest')
r10=Turtle();r10.color('orange');r10.speed('fastest')


r1.left(90)
r1.fd(-g-100);r1.fd(2*(g+100));r1.write('SHEAR STRESS',font=('arial',16,'bold'))   #axis
r2.fd(-((s3**2)**0.5)-g-100);r2.fd(2*(((s3**2)**0.5)+g+100))
r2.write('NORMAL STRESS',font=('arial',16,'bold'))

r3.penup();r3.goto(s1,t);r3.pendown();r3.goto(s2,-t)
#r3.write('('+str(s1)+','+str(t)+')' ,font=('arial',16,'bold'))

r4.penup();r4.goto(s2,-t);r4.pendown();r4.goto(s1,t)
#r4.write('('+str(s2)+','+str(-t)+')' ,font=('arial',16,'bold'))


r5.penup();r5.goto(s3,0);r5.left(90);r5.fd(g);r5.right(90);r5.pendown();r5.circle(-g)
r5.penup();r5.goto(s3,0)
r5.color('yellow');r5.left(90);r5.fd(g);r5.pendown();r5.fd(30)
r5.write(str(round(val,2)),font=('arial',10,'bold'))

r6.penup();r6.goto(s3+g,0);r6.pendown()
r6.write(str(round(m+val,2)),font=('arial',10,'bold'))
r7.penup();r7.goto(s3-g,0);r7.pendown()
r7.write(str(round(m-val,2)),font=('arial',10,'bold')) 

r8.penup();r8.goto(s3,0);r8.pendown();r8.left(ang);r8.left(o1);r8.fd(g)

p=list((r8.position()))
sa=p[0];ta=p[1]
c1=sa;c2=ta
sa=(sa/50)*div;ta=(ta/50)*div
res=(sa**2 + ta**2)**0.5


r8.write('('+str(round(sa,2))+','+str(round(ta,2))+')',font=('arial',9,'bold'))

r8.backward(2*g)

p1=list((r8.position()))
sa1=p1[0];ta1=p1[1]
c3=sa1;c4=ta1
sa1=(sa1/50)*div;ta1=(ta1/50)*div
res1=(sa1**2 + ta1**2)**0.5

r8.write('('+str(round(sa1,2))+','+str(round(ta1,2))+')',font=('arial',9,'bold'))

r8.ht()

r9.penup();r9.goto(s3,0);r9.left(ang);r9.left(o1);r9.fd(30);r9.right(90);r9.pendown();r9.circle(-30,(o1**2)**0.5)
r9.write(str(round(o1,3))+'degs',font=('arial',9,'bold'));r9.ht()

r10.ht();r10.goto(c1/2,c2/2);r10.write(str(round(res,2)),font=('arial',9,'bold'))
r10.goto(c1,c2);r10.goto(0,0)

r10.goto(c3/2,c4/2);r10.write(str(round(res1,2)),font=('arial',9,'bold'))
r10.goto(c3,c4)

mainloop()



