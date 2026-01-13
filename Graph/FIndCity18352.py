from collections import deque
import sys
input= sys.stdin.readline

def bfs(n):
    que= deque()
    que.append(n)
    V[n]= True
    cnt= 0
    while que:
        if cnt==K:
            return que
        cnt += 1
        ll= len(que)
        for _ in range(ll):
            nn= que.popleft()
            for e in G[nn]:
                if V[e]==False:
                    V[e]= True
                    que.append(e)

N, M, K, X= map(int,input().split())
G= [[] for _ in range(N)]
V= [False]*N
for _ in range(M):
    A, B= map(int,input().split())
    G[A-1].append(B-1)

R= []
R= bfs(X-1)
if R:
    R= list(R)
    R.sort()
    for i in range(len(R)):
        print(R[i]+1)
else:
    print(-1)