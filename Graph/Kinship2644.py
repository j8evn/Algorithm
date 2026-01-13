from collections import deque
import sys
input= sys.stdin.readline

def bfs(n):
    V= [False]*N
    que= deque([(n, 0)])
    V[n]= True
    while que:
        nn, cnt = que.popleft()
        if nn == b-1:
            return cnt
        for e in G[nn]:
            if not V[e]:
                V[e]= True
                que.append((e, cnt+1))
    return -1

N = int(input())
a, b = map(int, input().split())
M = int(input())
G = [[] for _ in range(N)]
for _ in range(M):
    x, y= map(int, input().split())
    x, y= x-1, y-1
    G[x].append(y)
    G[y].append(x)

print(bfs(a-1))
