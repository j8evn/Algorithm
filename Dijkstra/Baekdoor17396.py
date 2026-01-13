import heapq
import sys
input= sys.stdin.readline

def Dijkstra(fr):
    cost= [inf]*N
    V= [False]*N
    cost[fr]= 0
    heapq.heappush(pq, (cost[fr],fr))
    while pq:
        co, n= heapq.heappop(pq)
        if V[n]==True:
            continue
        V[n]= True
        for e in G[n]:
            if V[e]==True:
                continue
            if cost[e] > co+G[n][e]:
                cost[e]= co+ G[n][e]
                heapq.heappush(pq, (cost[e],e))
    return cost

inf= 10000000000
N, M= map(int,input().split())
A= list(map(int,input().split()))
A[-1]= 0
G= [{} for _ in range(N)]
for _ in range(M):
    u, v, w= map(int,input().split())
    t= min(w,G[u].get(v,inf))
    if A[u]==0 and A[v]==0:
        G[u][v], G[v][u]= t, t

pq= []
rr= Dijkstra(0)
if rr[N-1]>=inf:
    print(-1)
else:
    print(rr[N-1])