from collections import deque
import sys
input= sys.stdin.readline

T= int(input())
for _ in range(T):
    N, M= map(int,input().split())
    tt= list(map(int,input().split()))
    C, G= [0]*N, [[] for _ in range(N)]
    for _ in range(M):
        n1, n2= map(int,input().split())
        n1, n2= n1-1, n2-1
        G[n1].append(n2)
        C[n2]= C[n2]+1
    W= int(input())-1
    
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
    print(dp[W])