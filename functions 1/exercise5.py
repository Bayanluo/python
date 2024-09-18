#function exercises:
#1:
word1=input('enter a word:')
def odd (word1):
    r=''
    for i in range(len(word1)):
        if i%2==0:
            r+=word1[i]
    return r
print('the odd leter are:',odd(word1))

#2:
word2=input('enter a word:')
def vowels (word2):
    vl='A','a','E','e','O','o','U','u','I','i'
    n=0
    for i in word2:
        for j in vl:
            if i==j:
                n+=1
    print(n)
vowels(word2)

#3:
m1=int(input('enter mass1:'))
m2=int(input('enter mass2:'))
d=int(input('enter distance:'))
def gravity(m1,m2,d):
    g=6/693*(10**-8)
    f=(g*m1*m2)/(d**2)
    return f
print(gravity(m1,m2,d))

#3 with 2 function:
def gravity(m1,m2,d):
    g=6.693*(10**-8)
    f=(g*m1*m2)/(pow(d))
    return f
def main():
    m1=int(input('enter mass1:'))
    m2=int(input('enter mass2:'))
    d=int(input('enter distance:'))
    print(gravity(m1,m2,d))
main()
def pow(x):
    print(x*x)

#4:
import math
a=int(input('enter side a:'))
b=int(input('enter side b:'))
c=int(input('enter side c:'))
def s (a,b,c):
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('s=',s)
s(a,b,c)