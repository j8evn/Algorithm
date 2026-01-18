from collections import deque
import sys
input= sys.stdin.readline

ss= list(input().split())
n= int(input())
dq= deque()
for _ in range(n):
    dq.append(input().rstrip())

A, B= [], []
cnt= 1
while dq:
    cnt += 1
    for _ in range(len(ss)-1):
        dq.append(dq.popleft())
    if cnt%2==0:
        A.append(dq.popleft())
    elif cnt%2==1:
        B.append(dq.popleft())

print(len(A))
print("\n".join(A))
print(len(B))
print("\n".join(B))