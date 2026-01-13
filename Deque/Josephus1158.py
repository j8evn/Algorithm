from collections import deque

n, k= map(int,input().split())
dq, A= deque(), []
for i in range(n):
    dq.append(i+1)
while dq:
    for i in range(k-1):
        dq.append(dq.popleft())
    A.append(dq.popleft())
A= map(str,A)
print("<"+', '.join(A)+">")