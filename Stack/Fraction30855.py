import sys

def gcd(a,b):
    if (a<b):
        a, b= b, a
    while (b>0):
        if (a%b==0):
            return b
        a, b= b, a%b

def Frac(a,b,c):
    d1, n1= a[0], a[1]
    d2, n2= b[0]*c[1], b[1]*c[0]
    dd, nn= d1*n2 + d2*n1, n1*n2
    g= gcd(dd,nn)
    return [dd//g,nn//g]

def Calc(ss):
    for i in range(N):
        if ss[i]=='(':
            Stack.append('(')
        elif ss[i]==')':
            if len(Stack)<4:
                return -1
            n3= Stack.pop()
            n2= Stack.pop()
            n1= Stack.pop()
            n0= Stack.pop()
            if (len(n3)!=2) or (len(n2)!=2) or (len(n1)!=2) or (n0!='('):
                return -1
            t= Frac(n1,n2,n3)
            Stack.append(t)
        else:
            n= int(ss[i])
            Stack.append([n,1])
    return 1

N= int(input())
ss= list(input().split())
Stack= []
ans= Calc(ss)
if ans==-1:
    print(-1)
elif len(Stack)!=1:
    print(-1)
else:
    print(Stack[-1][0], Stack[-1][1])