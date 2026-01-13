import heapq

def CheckSet(e,co,add):
    if e<0 or e>=M:
        return
    if V[e]==True:
        return
    if C[e] > co+add:
        C[e]= co+ add
        heapq.heappush(pq, (C[e],e))

def DijkPq(fr,to):
    heapq.heappush(pq, (0,fr))
    while pq:
        co, n= heapq.heappop(pq)
        if V[n]==True:
            continue
        if n==to:
            return co
        V[n]= True
        CheckSet(n-1,co,1)
        CheckSet(n+1,co,1)
        CheckSet(2*n,co,0)

M= 100001
L= 999999999
C= [L]*M
V= [False]*M
pq= []
N, K= map(int,input().split())
print(DijkPq(N,K))