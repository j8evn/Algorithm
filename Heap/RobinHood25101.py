import heapq

N, K= map(int,input().split())
A= list(map(int,input().split()))
pq= []
for i in range(N):
    heapq.heappush(pq,(-A[i],i))

while K!=0:
    mm, mi= heapq.heappop(pq)
    mm= -mm
    if mm<=100:
        break
    heapq.heappush(pq,(-(mm-100),mi))
    K= K-1

if K==0:
    R= []
    for _ in range(N):
        mm, mi= heapq.heappop(pq)
        mm= -mm
        R.append([mm,mi])
    R.sort(key=lambda x:x[1])
    ans= []
    for i in range(N):
        ans.append(R[i][0])
    print(*ans)
else:
    print("impossible")