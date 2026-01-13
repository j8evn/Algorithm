import sys
iput= sys.stdin.readline

n= int(input())
A= list(map(int,input().split()))
x= int(input())
A.sort()

l, r= 0, n-1
cnt= 0
while l<r:
    if A[l]+A[r] == x:
        cnt += 1
        l= l+1
        r= r-1
    elif A[l]+A[r] > x:
        r= r-1
    elif A[l]+A[r] < x:
        l= l+1
print(cnt)