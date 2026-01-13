from collections import deque
import sys
input= sys.stdin.readline

N= int(input())
dq= deque()
for _ in range(N):
  D= list(input().split())
  if D[0]=="push_front":
    dq.appendleft(D[1])
  elif D[0]=="push_back":
    dq.append(D[1])
  elif D[0]=="pop_front":
    if dq:
      print(dq.popleft())
    else:
      print(-1)
  elif D[0]=="pop_back":
    if dq:
      print(dq.pop())
    else:
      print(-1)
  elif D[0]=="size":
    print(len(dq))
  elif D[0]=="empty":
    if dq:
      print(0)
    else:
      print(1)
  elif D[0]=="front":
    if dq:
      print(dq[0])
    else:
      print(-1)
  elif D[0]=="back":
    if dq:
      print(dq[-1])
    else:
      print(-1)