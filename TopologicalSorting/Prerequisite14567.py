import sys
from collections import deque
input= sys.stdin.readline

a, b= map(int,input().split())
G= [[] for _ in range(a)]
C= [0 for _ in range(a)]
dp= [0 for _ in range(a)]
for i in range(b):
    x, y= map(int,input().split())
    x, y= x-1, y-1
    C[y] += 1
    G[x].append(y)

que= deque()
for i in range(a):
    if C[i]==0:
        que.append(i)
        dp[i]= 1
while que:
    r= que.popleft()
    for i in G[r]:
        C[i] -= 1
        dp[i]= dp[r]+1        
        if C[i]==0:
            que.append(i)
print(*dp)