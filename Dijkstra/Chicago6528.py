import heapq
import sys
input= sys.stdin.readline

def Dijkstra(fr):
    cost= [-1]*N
    V= [False]*N
    cost[fr]= 1
    heapq.heappush(pq, (-cost[fr],fr))
    while pq:
        co, n= heapq.heappop(pq)
        co= -co
        if V[n]==True:
            continue
        V[n]= True
        for e in G[n]:
            if V[e]==True:
                continue
            if cost[e] < (co*G[n][e])/100:
                cost[e]= (co*G[n][e])/100
                heapq.heappush(pq, (-cost[e],e))
    return cost

inf= 100000000
while True:
    A= list(map(int,input().split()))
    if len(A)==1:
        break
    else:
        N, M= A[0], A[1]
    G= [{} for _ in range(N)]
    for _ in range(M):
        u, v, w= map(int,input().split())
        u, v= u-1, v-1
        t= min(w,G[u].get(v,inf))
        G[u][v], G[v][u]= t, t

    pq= []
    rr= Dijkstra(0)
    print("{:.6f} percent".format(100*rr[N-1]))