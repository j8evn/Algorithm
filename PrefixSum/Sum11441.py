import sys
input= sys.stdin.readline

N= int(input())
A= list(map(int,input().split()))
for i in range(1,N):
    A[i] += A[i-1]
M= int(input())
R= []
for _ in range(M):
    a, b= map(int,input().split())
    i, j= a-2, b-1
    if i==-1:
        R.append(A[j])
    else:
        R.append(A[j]-A[i])
R= map(str,R)
print('\n'.join(R))