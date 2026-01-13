import sys
input= sys.stdin.readline

N, M= map(int,input().split())
A= list(map(int,input().split()))
A.sort()
s, e= 1, A[-1]*2

while s<=e:
    mid= (s+e)//2
    cnt= 0
    for i in range(len(A)):
        if A[i]>mid:
            cnt += A[i]-mid
    if cnt>=M:
        s= mid+1
    else:
        e= mid-1
print(e)