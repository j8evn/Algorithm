import heapq
import sys
input= sys.stdin.readline

N= int(input())
A= []
for _ in range(N):
    A.append(list(map(int,input().split())))
A.sort(key=lambda x:x[1])

pq= []
R, num= [0]*N, 1
heapq.heappush(pq,(A[0][2],num))
R[A[0][0]-1]= num
for i in range(1,N):
    if pq[0][0]>A[i][1]:
        num += 1
        heapq.heappush(pq,(A[i][2],num))
        R[A[i][0]-1]= num
    else:
        a, n= heapq.heappop(pq)
        heapq.heappush(pq,(A[i][2],n))
        R[A[i][0]-1]= n

print(len(pq))
print(*R, sep='\n')