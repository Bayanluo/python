#loops.pdf
#1:
for i in range(1,9):
    for j in range(9,i,-1):
        print(i,end=' ')
    print()

#2:
for i in range(7,0,-1):
    for j in range(i,0,-1):
        print(j, end=' ')
    print()

#3:
for i in range(1,5):
    for j in range(1,7):
        print('$',end='')
    print()

#4:
for i in range(1,9):
    for j in range(1,i+1):
        print(i,end=' ')
    print()