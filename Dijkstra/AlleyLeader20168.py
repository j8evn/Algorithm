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
N= int(input())
A, B, C= map(int,input().split())
M= int(input())
G= [{} for _ in range(N)]
for _ in range(M):
    u, v, w= map(int,input().split())
    u, v= u-1, v-1
    t= min(w,G[u].get(v,inf))
    G[u][v], G[v][u]= t, t

pq= []
ra= Dijkstra(A-1)
rb= Dijkstra(B-1)
rc= Dijkstra(C-1)
r= []
for i in range(N):
    r.append(min(min(ra[i],rb[i]),rc[i]))
print(r.index(max(r))+1)