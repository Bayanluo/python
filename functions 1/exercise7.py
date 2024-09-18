#function exercises2:
#1:
import math
def cold (v,t):
    w=33-(((10*(math.sqrt(v))-v+10.5)*(33-t))/(23-1))
    print('cold wind=',w)   
def main1 ():
    v=int(input('enter wind speed(m/s):'))
    t=int(input('enter temperature(c):'))
    print(cold(v,t))
main1()

#2:
def repeated (n,d):
    c=0
    for i in n:
        if i==d:
            c+=1
    print('Repeated digit',d,':',c)
def main2():
    n=input('enter a number:')
    d=input('enter a digit:')
    print(repeated(n,d))
main2()
#3:
def two (n1,n2):
    s=abs(n1-n2)
    m=(n1*n2)
    d1=(n1/n2)
    d2=(n2/n1)
    print('ln1-n2l=',s,'n1*n2=',m,'n1/n2=',d1,'n2/n1=',d2)
def main3():
    n1=int(input('enter the first number:'))
    n2=int(input('enter the secend number:'))
    print(two(n1,n2))
main3()