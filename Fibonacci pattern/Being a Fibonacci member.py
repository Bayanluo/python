f1=0
f2=1
f3=1
n=int(input('enter a number:'))
while n>f3:
    f3=f1+f2
    f1=f2
    f2=f3
if n==f3:
    print('yes')
else:
    print('no')
