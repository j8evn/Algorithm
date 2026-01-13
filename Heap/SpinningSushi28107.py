import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A, B = [], []
for i in range(N):
    tt = list(map(int, input().split()))
    for j in range(1, len(tt)):
        heapq.heappush(A, (tt[j], i))
tt = list(map(int, input().split()))
for x in tt:
    heapq.heappush(B, x)

R = [0] * N
while A and B:
    a1, a2 = heapq.heappop(A)
    b = heapq.heappop(B)
    if b == a1:
        R[a2] += 1
    elif b > a1:
        heapq.heappush(B, b)
    elif b < a1:
        heapq.heappush(A, (a1, a2))

print(*R)
