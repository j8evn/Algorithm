import sys
input= sys.stdin.readline

N= int(input())
A= []
for _ in range(N):
    A.append(input().strip())
A.sort()
print(A)