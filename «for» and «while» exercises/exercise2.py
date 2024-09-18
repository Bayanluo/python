#string ex.pdf
#1:
import random
a1=[1,2,3,4,5,6,7,8,9]
random.shuffle(a1)
print(a1[0])

#2:
#?

#3:
word=input('enter a word:')
n=int(len(word))
if n%2!=0:
    m=int((n-1)/2)
    print(word[m])
else:
    print('does not have')

#4:
alphabet=['0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
name=input('enter a name:')
s=0
for i in name:
    for j in alphabet:
        if i==j:
            s+=alphabet.index(j)
print(s)

#5:
word2=input('enter a word:')
s2=int(len(word2))
words=word2[s2:0]
if word2==words:
    print('yes')
else:
    print('no')

#6:
a6=input('enter the first word:')    
b6=input('enter the second word:')     
for i in a6:
    for j in b6:
        if i==j:
            print(i)

