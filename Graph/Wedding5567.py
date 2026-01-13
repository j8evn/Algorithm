from collections import deque

def bfs(n):
    que= deque()
    que.append(n)
    V[n]= True
    cnt, t= 0, 0
    while que:
        if t==3:
            break
        t += 1
        for _ in range(len(que)):
            nn= que.popleft()
            cnt += 1
            for e in G[nn]:
                if V[e]==False:
                    V[e]= True
                    que.append(e)
    return cnt

N= int(input())
M= int(input())
V= [False]*N
G= [[] for _ in range(N)]
for _ in range(M):
    n1, n2= map(int,input().split())
    n1, n2= n1-1, n2-1
    G[n1].append(n2)
    G[n2].append(n1)

print(bfs(0)-1)