import math
import sys
input= sys.stdin.readline

N= int(input())
A= []
for _ in range(N):
    A.append(int(input()))

t= math.gcd(A[1]-A[0],A[2]-A[1])
for i in range(1,N):
    t= math.gcd(t,A[i]-A[i-1])

cnt= 0
for i in range(1,N):
    cnt += ((A[i]-A[i-1])//t-1)
print(cnt)