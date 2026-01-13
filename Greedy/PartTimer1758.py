import sys
input= sys.stdin.readline

N= int(input())
A= []
for i in range(N):
    A.append(int(input()))
A.sort(reverse=True)

m= 0
for i in range(N):
    if A[i]-i<0:
        break
    m += (A[i]-i)
print(m)