from collections import deque
import sys
input= sys.stdin.readline

def bfs(n,f):
    que= deque()
    if n!=f:
        V[n]= True
    que.append(n)
    while que:
        nn= que.popleft()
        B.append(nn)
        if len(B)>1 and nn==f:
            return True
        for e in G[nn]:
            if V[e]==False:
                V[e]= True
                que.append(e)
    return False

N= int(input())
G= [[] for _ in range(N)]
for i in range(N):
    tt= list(map(int,input().split()))
    for j in range(len(tt)):
        if tt[j]==1:
            G[i].append(j)

R= [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        V= [False]*N
        B= []
        if bfs(i,j)==True:
            R[i][j]= 1

for i in range(N):
    print(*R[i])