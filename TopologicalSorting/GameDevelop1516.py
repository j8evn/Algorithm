from collections import deque
import sys
input= sys.stdin.readline

N= int(input())
tt= []
C, G= [0]*N, [[] for _ in range(N)]
for i in range(N):
    k= list(map(int,input().split()))
    tt.append(k[0])
    for j in range(1,len(k)):
        if k[j]==-1:
            break
        G[k[j]-1].append(i)
        C[i]= C[i]+1

dp= [0]*N
Q= deque()
for i in range(N):
    if C[i]==0:
        Q.append(i)
        dp[i]= tt[i]
while Q:
    n= Q.popleft()
    for t in G[n]:
        dp[t]= max(dp[t],dp[n]+tt[t])
        C[t]= C[t]-1
        if C[t]==0:
            Q.append(t)

dp= map(str,dp)
print('\n'.join(dp))