import sys
input= sys.stdin.readline

N= int(input())
A= []
for _ in range(N):
    A.append(int(input()))
A.sort(reverse=True)

r= -1
for i in range(2,N):
    if A[i-2]<A[i-1]+A[i]:
        r= A[i-2]+A[i-1]+A[i]
        break
print(r)