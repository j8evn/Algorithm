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

N, E= map(int,input().split())
K= int(input())-1
G= []
for _ in range(N):
    G.append({})
for i in range(E):
    u, v, w= map(int,input().split())
    u, v= u-1, v-1
    G[u][v]= min(w,G[u].get(v,99999999))
inf= 100000000
pq= []
rr= Dijkstra(K)
for i in range(N):
    if rr[i]==inf:
        print('INF')
    else:
        print(rr[i])