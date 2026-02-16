from collections import deque
import sys
input= sys.stdin.readline

def bfs(n):
    que= deque()
    V[n]= True
    que.append(n)
    cnt= 0
    while que:
        nn= que.popleft()
        cnt += 1
        for e in G[nn]:
            if V[e]==True:
                continue
            V[e]= True
            que.append(e)
    return cnt

N, M= map(int,input().split())
G= [[] for _ in range(N)]
V= [False]*N
for _ in range(M):
    u, v= map(int,input().split())
    u, v= u-1, v-1
    G[u].append(v)
    G[v].append(u)

mm= 0
for i in range(N):
    if V[i]==True:
        continue
    mm= max(mm, bfs(i))
print(mm)