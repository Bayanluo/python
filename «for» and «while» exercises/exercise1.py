#for wile.pdf
while True:
    n=int(input('enter:'))
    s1=0
    for i in range(1,n):
        if (n%i==0):
            s1+=i
    if s1==n:
        print('its perfected')
    else:
        print('its not perfected')
    c=input('do you want to continiu?(yes/no)')
    if c[0]=='n'or c[0]=='N':
        break
    
# #1:
number=int(input('enter the number:'))
if number>0:
    print('+')
elif number==0:
    print('0')
else:
    print('-')

#2:
n=int(input('enter a number:'))
for i in range(n,1,-1):#7654321
    if i%5==0:
        print(i)

#3:
a=['a','u','o','e']
word=input('enter a word:')
n=0
for i in word:
    if i in a:
        n+=1
print(n)

#4:
i=input('enter_ _ _:')
n=int(i)
a4=int(i[0])
b4=int(i[1])
c4=int(i[2])
m=100*c4+10*b4+a4
if n==m:
    print('yes')
else : 
    print('no')

#5:
for i in range(1,10):
    for j in range (i,10):
        print(i,end=' ')
    print()

#6:
number=int(input('enter the number:'))
i=1
while i<=number:
    id=int(input('enter the ID:'))
    h=int(input('enter the hour:'))
    m=int(input('enter the mony per hour:'))
    a=0
    if h>40:
        a=(40*m)+((h-40)*(m/2)) 
    else:
        a=h*m
    print('id=', id, 'mony=', a)
    i+=1