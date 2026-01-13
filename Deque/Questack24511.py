from collections import deque
import sys
input= sys.stdin.readline

N= int(input())
A= list(map(int,input().split()))
B= list(map(int,input().split()))
M= int(input())
C= list(map(int,input().split()))

questack= deque()
for i in range(N):
    if A[i]==0:
        questack.appendleft(B[i])

R= []
for i in range(M):
    questack.append(C[i])
    R.append(questack.popleft())
print(*R)