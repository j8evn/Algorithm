import sys
input= sys.stdin.readline

def IsPalin(a):
    l, r= 0, len(a)-1
    while (l<r):
        if a[l] != a[r]:
            return False
        l, r= l+1, r-1
    return True

def Nary(n,b):
    d= []
    while (n>0):
        d.append(n%b)
        n= n//b
    return d

def Check(n):
    for i in range(2,65):
        Nar= Nary(n,i)
        if IsPalin(Nar)==True:
            return True
    return False

N= int(input())
for i in range(N):
    n= int(input())
    if Check(n)==True:
        print(1)
    else:
        print(0)
