import heapq
import sys
input= sys.stdin.readline

R= []
leftpq, rightpq= [], []
N= int(input())
for _ in range(N):
    n= int(input())
    if len(leftpq)==len(rightpq):
        heapq.heappush(leftpq,-n)
    else:
        heapq.heappush(rightpq,n)
    if leftpq:
        if rightpq:
            tt1= -heapq.heappop(leftpq)
            tt2= heapq.heappop(rightpq)
            if tt1>tt2:
                heapq.heappush(leftpq,-tt2)
                heapq.heappush(rightpq,tt1)
            else:
                heapq.heappush(leftpq,-tt1)
                heapq.heappush(rightpq,tt2)
    tt= -heapq.heappop(leftpq)
    R.append(tt)
    heapq.heappush(leftpq,-tt)

R= map(str,R)
print('\n'.join(R))