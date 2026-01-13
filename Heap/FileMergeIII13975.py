import heapq
import sys
input= sys.stdin.readline

T= int(input())
for _ in range(T):
    K= int(input())
    A= list(map(int,input().split()))
    pq= []
    for i in range(K):
        heapq.heappush(pq,A[i])
    s= 0
    while len(pq)>1:
        t= heapq.heappop(pq)+heapq.heappop(pq)
        s += t
        heapq.heappush(pq,t)
    print(s)