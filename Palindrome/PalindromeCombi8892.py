import sys
input= sys.stdin.readline

def IsPalin(a):
    l, r= 0, len(a)-1
    while (l<r):
        if a[l] != a[r]:
            return False
        l, r= l+1, r-1
    return True

def Com(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if i==j:
                continue
            if IsPalin(A[i]+A[j])==True:
                return A[i]+A[j]
    return False

T= int(input())
for _ in range(T):
    k= int(input())
    A= []
    for _ in range(k):
        A.append(input().strip())
    R= Com(A)
    if R==False:
        print(0)
    else:
        print(R)