import heapq
import sys
input= sys.stdin.readline

T= int(input())
for _ in range(T):
    N= int(input())
    mxheap, mnheap= [], []
    V= [False]*N
    for i in range(N):
        O, n= input().split()
        n= int(n)
        if O== 'I':
            heapq.heappush(mxheap, (-n,i))
            heapq.heappush(mnheap, (n,i))
            V[i]= True
        elif O== 'D':
            if n==1:
                while mxheap and V[mxheap[0][1]]==False:
                    heapq.heappop(mxheap)
                if mxheap:
                    V[mxheap[0][1]]= False
                    heapq.heappop(mxheap)
            elif n==-1:
                while mnheap and V[mnheap[0][1]]==False:
                    heapq.heappop(mnheap)
                if mnheap:
                    V[mnheap[0][1]]= False
                    heapq.heappop(mnheap)

    while mxheap and V[mxheap[0][1]]==False:
        heapq.heappop(mxheap)
    while mnheap and V[mnheap[0][1]]==False:
        heapq.heappop(mnheap)

    if not mxheap or not mnheap:
        print("EMPTY")
    else:
        print(-mxheap[0][0], mnheap[0][0])