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

inf= 100000000
N, M, X= map(int,input().split())
G= [{} for _ in range(N)]
for _ in range(M):
    u, v, w= map(int,input().split())
    u, v= u-1, v-1
    t= min(w,G[u].get(v,inf))
    G[u][v]= t

pq= []
rr= Dijkstra(X-1)
for i in range(N):
    rr2= Dijkstra(i)
    rr[i] += rr2[X-1]
print(max(rr))