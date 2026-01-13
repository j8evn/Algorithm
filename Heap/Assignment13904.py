import heapq
import sys
input= sys.stdin.readline

N= int(input())
pq= []
mm= 0
for _ in range(N):
    d, w= map(int,input().split())
    heapq.heappush(pq,(-w,d))
    mm= max(mm,d)

v= [False]*(mm+1)
s= 0
while pq:
    w, d= heapq.heappop(pq)
    w= -w
    for i in range(d,0,-1):
        if v[i]==True:
            continue
        v[i]= True
        s += w
        break
print(s)