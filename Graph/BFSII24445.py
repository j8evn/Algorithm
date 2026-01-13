from collections import deque
import sys
input= sys.stdin.readline

def bfs(n):
    que= deque()
    V[n]= True
    que.append(n)
    while que:
        nn= que.popleft()
        B.append(nn)
        for e in G[nn]:
            if V[e]==True:
                continue
            V[e]= True
            que.append(e)

N, M, R= map(int,input().split())
G= [[] for _ in range(N)]
V= [False]*N
for _ in range(M):
    u, v= map(int,input().split())
    u, v= u-1, v-1
    G[u].append(v)
    G[v].append(u)
for i in range(N):
    G[i].sort(reverse=True)

B= []
rr= [0]*N
bfs(R-1)
for i in range(len(B)):
    rr[B[i]]= i+1
rr= map(str,rr)
print('\n'.join(rr))