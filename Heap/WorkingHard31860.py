import heapq
import sys
input= sys.stdin.readline

N, M, K= map(int,input().split())
pq= []
for _ in range(N):
    heapq.heappush(pq, -int(input()))

cnt= 0
s= 0
R= []
t= -heapq.heappop(pq)
while t>K:
    cnt += 1
    s= (s//2+t)
    R.append(s)
    heapq.heappush(pq,-(t-M))
    t= -heapq.heappop(pq)
print(cnt)
R= map(str,R)
print('\n'.join(R))