from collections import deque
import sys
input= sys.stdin.readline

def bfs(n):
    que= deque()
    V[n]= True
    que.append(n)
    while que:
        nn= que.popleft()
        R.append(nn)
        for e in G[nn]:
            if V[e]==True:
                continue
            V[e]= True
            que.append(e)

N= int(input())
M= int(input())
V=[False]*N
G= [[] for _ in range(N)]
for _ in range(M):
    a, b= map(int,input().split())
    a, b= a-1, b-1
    G[a].append(b)
    G[b].append(a)
R= []
bfs(0)
print(len(R)-1)