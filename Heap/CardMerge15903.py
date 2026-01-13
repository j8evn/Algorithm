import heapq

n, m= map(int,input().split())
A= list(map(int,input().split()))
pq= []
for i in range(n):
    heapq.heappush(pq,A[i])

for _ in range(m):
    x= heapq.heappop(pq)
    y= heapq.heappop(pq)
    heapq.heappush(pq,x+y)
    heapq.heappush(pq,x+y)
print(sum(pq))