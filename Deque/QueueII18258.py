from collections import deque
import sys
input= sys.stdin.readline

N= int(input())
dq= deque()
for _ in range(N):
    ll= list(input().split())
    if ll[0]=="push":
        dq.append(int(ll[1]))
    elif ll[0]=="pop":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif ll[0]=="size":
        print(len(dq))
    elif ll[0]=="empty":
        if dq:
            print(0)
        else:
            print(1)
    elif ll[0]=="front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif ll[0]=="back":
        if dq:
            print(dq[-1])
        else:
            print(-1)