import sys
input= sys.stdin.readline

N= int(input())
A= []
for _ in range(N):
    A.append(int(input()))
A.sort()

mm= -1
for a in A:
    mm= max(mm, a*N)
    N -= 1
print(mm)