a=int(input('enter a number:'))
a1=0
a2=1
a3=1
while a2<a:
    a3=a1+a2 
    a1=a2
    a2=a3
if a==a3:
    print('yes')