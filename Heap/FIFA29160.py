import heapq
import sys
input= sys.stdin.readline

P= [[] for _ in range(11)]
N, K= map(int,input().split())
for _ in range(N):
    p, w= map(int,input().split())
    heapq.heappush(P[p-1],-w)

for _ in range(K):
    for i in range(11):
        if P[i]:
            heapq.heappush(P[i],-(-heapq.heappop(P[i])-1))

cnt= 0
for i in range(11):
    if P[i]:
        k= -(heapq.heappop(P[i]))
        if k<0:
            k= 0
        cnt += k
print(cnt)