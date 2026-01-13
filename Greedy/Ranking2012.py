import sys
input= sys.stdin.readline

N= int(input())
A= []
for _ in range(N):
    A.append(int(input()))
A.sort()

s= 0
for i in range(N):
    s += abs(i+1-A[i])
print(s)