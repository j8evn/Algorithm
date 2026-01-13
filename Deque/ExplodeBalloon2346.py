from collections import deque

N= int(input())
dq= deque(enumerate(map(int,input().split()), start=1))
R= []
for i in range(N):
    p= dq.popleft()
    R.append(p[0])
    if p[1]>0:
        dq.rotate(-(p[1]-1))
    else:
        dq.rotate(-p[1])
R= map(str,R)
print(' '.join(R))