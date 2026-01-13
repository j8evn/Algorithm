import heapq
import sys
input= sys.stdin.readline

N= int(input())
pq= []
for _ in range(N):
    ll= list(map(int,input().split()))
    for i in range(len(ll)):
        if len(pq)<N:
            heapq.heappush(pq,ll[i])
        else:
            heapq.heappush(pq,ll[i])
            heapq.heappop(pq)
print(pq[0])