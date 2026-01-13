import heapq
import sys
input= sys.stdin.readline

N, D= map(int,input().split())
W, M= [], []
for _ in range(N):
    a, x= map(int,input().split())
    if a==1:
        heapq.heappush(M,x)
    else:
        heapq.heappush(W,x)

cnt= len(W)
while M:
    while W and M[0]>=D:
        D *= heapq.heappop(W)
    if M[0]<D:
        D += heapq.heappop(M)
        cnt += 1
    else:
        break
print(cnt)