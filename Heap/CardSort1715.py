import heapq
import sys
input= sys.stdin.readline

N= int(input())
pq= []
cnt= 0
for _ in range(N):
    heapq.heappush(pq,int(input()))
while len(pq)>1:
    n1= heapq.heappop(pq)
    n2= heapq.heappop(pq)
    cnt += (n1+n2)
    heapq.heappush(pq,n1+n2)
print(cnt)