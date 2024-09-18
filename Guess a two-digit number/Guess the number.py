import random
a=random.randint(10,99)
b=int(input('Choose the level:(1. Easy 2. Medium 3. Hard)'))
if b==1:
    x=10
elif b==2:
    x=6
else:
    x=4
while 0<x :
    x-=1
    c=int(input('Enter your guess:'))
    if a<c:
        print('My number is smaller than',c)
    elif c<a:
        print('My number is greater than',c)
    if a==c: 
        print('You won! That is right!')
        break 
print('game over')
