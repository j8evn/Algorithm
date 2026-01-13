import heapq
import sys
input= sys.stdin.readline

T= int(input())
for _ in range(T):
    R= []
    leftpq, rightpq= [], []
    N= int(input())
    A= list(map(int,input().split()))
    if N%10==0:
        for i in range(N//10-1):
            A.extend(list(map(int,input().split())))
    else:
        for i in range(N//10):
            A.extend(list(map(int,input().split())))

    for i in range(N):
        if len(leftpq)==len(rightpq):
            heapq.heappush(leftpq,-A[i])
        else:
            heapq.heappush(rightpq,A[i])
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
        if (i+1)%2==1:
            R.append(-leftpq[0])

    ll = len(R)
    if ll>10:
        s= 0
        e= 10
        print(ll)
        for i in range(ll//10):
            print(*R[s:e])
            s += 10
            e += 10
        else:
            print(*R[s:])
    else:
        print(ll)
        print(*R)