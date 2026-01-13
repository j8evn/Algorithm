import sys
import heapq
input= sys.stdin.readline

pq= []
n= int(input())
for i in range(n):
    x= int(input())
    if x==0:
        if pq:
            print(heapq.heappop(pq)[1])
        else:
            print(0)
    else:
        heapq.heappush(pq,[abs(x),x])