import heapq
import sys
input= sys.stdin.readline

N= int(input())
pq= []
mm= 0
for _ in range(N):
    p, d= map(int,input().split())
    heapq.heappush(pq,(-p,d))
    mm= max(mm,d)

v= [False]*(mm+1)
s= 0
while pq:
    p, d= heapq.heappop(pq)
    p= -p
    for i in range(d,0,-1):
        if v[i]==True:
            continue
        v[i]= True
        s += p
        break
print(s)