import heapq
import sys
input = sys.stdin.readline

N= int(input())
A= []
for _ in range(N):
    A.append(list(map(int,input().split())))
A.sort(key=lambda x:x[0])

pq= []
heapq.heappush(pq, A[0][1])
for i in range(1, N):
    if pq[0] <= A[i][0]:
        heapq.heappop(pq)
    heapq.heappush(pq, A[i][1])
print(len(pq))