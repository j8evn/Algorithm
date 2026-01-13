# 유향 그래프, 부분순서집합 일 때

from collections import deque
import sys
input= sys.stdin.readline

N, M= map(int,input().split())
C, G= [0]*N, [[] for _ in range(N)]
for _ in range(M):
    n1, n2= map(int,input().split())
    n1, n2= n1-1, n2-1
    G[n1].append(n2)
    C[n2]= C[n2]+1
    
Q= deque()
for i in range(N):
    if C[i]==0:
        Q.append(i)
R= []
while Q:
    n= Q.popleft()
    R.append(n+1)
    for t in G[n]:
        C[t]= C[t]-1
        if C[t]==0:
            Q.append(t)
print(*R)