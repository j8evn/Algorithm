import heapq

N, M= map(int,input().split())
A= list(map(int,input().split()))
maxpq= []
for i in range(N):
    heapq.heappush(maxpq,-A[i])
minpq= []
for _ in range(M):
    if maxpq:
        heapq.heappush(minpq,-heapq.heappop(maxpq))

while maxpq and minpq:
    cur= -heapq.heappop(maxpq)
    heapq.heappush(minpq, heapq.heappop(minpq)+cur)
print(max(minpq))