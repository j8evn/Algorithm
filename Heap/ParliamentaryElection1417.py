import heapq

N= int(input())
d= int(input())
if N==1:
    print(0)
else:
    pq= []
    for _ in range(1,N):
        heapq.heappush(pq,-int(input()))
    cnt= 0
    while True:
        t= -heapq.heappop(pq)
        if t<d:
            break
        heapq.heappush(pq,-(t-1))
        d += 1
        cnt += 1
    print(cnt)