from collections import deque
import sys
input= sys.stdin.readline

N= int(input())
dq= deque()
for _ in range(N):
    dd= list(map(int,input().split()))
    if dd[0]==1:
        dq.appendleft(dd[1])
    elif dd[0]==2:
        dq.append(dd[1])
    elif dd[0]==3:
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif dd[0]==4:
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif dd[0]==5:
        print(len(dq))
    elif dd[0]==6:
        if dq:
            print(0)
        else:
            print(1)
    elif dd[0]==7:
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif dd[0]==8:
        if dq:
            print(dq[-1])
        else:
            print(-1)