import heapq
import sys
input= sys.stdin.readline

N, K= map(int,input().split())
pq= []
for _ in range(N):
    M, V= map(int,input().split())
    heapq.heappush(pq,(-V,M))
C= int(input())

ss= 0
while K!=0:
    V, M= heapq.heappop(pq)
    if M<=C:.
        ss += -V
        K -= 1
