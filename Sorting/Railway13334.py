# 우선순위큐: 값이 작은 순서로 빠져나옴 (시간복잡도: O(logN))

import heapq
import sys
input= sys.stdin.readline

n= int(input())
A= []
for i in range(n):
    x, y= map(int,input().split())
    if x>y:
        x, y= y, x
    A.append([x,y])
A.sort(key=lambda x:x[1])
L= int(input())

pq= []
mm= 0
for i in range(n):
    heapq.heappush(pq,A[i][0])
    while (len(pq)>0 and A[i][1]-L>pq[0]):
        heapq.heappop(pq)
    mm= max(mm,len(pq))
print(mm)
