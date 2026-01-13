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
N, M= map(int,input().split())
G= [{} for _ in range(N)]
for _ in range(M):
    u, v, w= map(int,input().split())
    u, v= u-1, v-1
    G[u][v]= min(w,G[u].get(v,inf))
    G[v][u]= min(w,G[u].get(v,inf))
s, t= map(int,input().split())

pq= []
rr= Dijkstra(s-1)
print(rr[t-1])