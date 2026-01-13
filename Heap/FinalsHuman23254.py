import heapq
import sys
input= sys.stdin.readline

N, M= map(int,input().split())
N= 24*N
A= list(map(int,input().split()))
B= list(map(int,input().split()))
pq= []
for i in range(M):
    heapq.heappush(pq, (-B[i],A[i]))

ss= 0
pq2= []
while pq:
    b, a= heapq.heappop(pq)
    b= -b
    if (100-a)%b==0:
        while N>0 and a+b<=100:
            a += b
            N= N-1
        print(a)
        ss += a
    else:
        heapq.heappush(pq2, (-b, a))
while pq2:
    b, a= heapq.heappop(pq2)
    b= -b
    while N>0 and a+b<=100:
        a += b
        N= N-1
    print(a)
    ss += a
print(ss)