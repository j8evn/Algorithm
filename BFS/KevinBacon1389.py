from collections import deque
import sys
input= sys.stdin.readline

def bfs(n, N, G):
    d= [-1]*(N+1)
    d[n]= 0
    que= deque([n])
    while que:
        cur= que.popleft()
        for g in G[cur]:
            if d[g] == -1:
                d[g]= d[cur]+ 1
                que.append(g)
    return sum(i for i in d if i!=-1)

N, M= map(int, input().split())
G= [[] for _ in range(N+1)]

for _ in range(M):
    u, v= map(int, input().split())
    G[u].append(v)
    G[v].append(u)
    
res= []
for i in range(1, N+1):
    res.append(bfs(i,N,G))

print(res.index(min(res))+1)