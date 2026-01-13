from collections import deque
import sys
input= sys.stdin.readline

def bfs(n):
    V= [False]*N
    que= deque()
    que.append(n)
    V[n]= True
    cnt= 0
    while que:
        nn= que.popleft()
        if len(G[nn])==1:
            cnt += 1
        for e in G[nn]:
            if V[e]==False:
                V[e]= True
                que.append(e)
    return cnt

N= int(input())
G= [[] for _ in range(N)]
for _ in range(N-1):
    n1, n2= map(int,input().split())
    G[n1].append(n2)
    G[n2].append(n1)
#print(G)
#print(bfs(0))
print((bfs(0)+1)//2)
