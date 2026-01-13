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
                idx[e]= n # 어디서 왔는지 저장
                heapq.heappush(pq, (cost[e],e))
    return cost

inf= 100000000
N= int(input())
M= int(input())

G= [{} for _ in range(N)]
for _ in range(M):
    u, v, w= map(int,input().split())
    u, v= u-1, v-1
    G[u][v]= min(w,G[u].get(v,inf))
s, a= map(int,input().split())
s, a= s-1, a-1

pq= []
idx= [-1]*N
rr= Dijkstra(s)
idx2= []
i= a
while idx[i]!=-1:
    idx2.append(i+1)
    i= idx[i]
idx2.append(i+1)
idx2.reverse()

print(rr[a])
print(len(idx2))
print(*idx2)