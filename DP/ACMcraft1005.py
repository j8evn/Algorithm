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
    Q, front, rear= [0]*N, 0, 0
    for i in range(N):
        if C[i]==0:
            Q[rear], rear= i, rear+1
            dp[i]= tt[i]
    while front<rear:
        n, front= Q[front], front+1
        for t in G[n]:
            dp[t]= max(dp[t],dp[n]+tt[t])
            C[t]= C[t]-1
            if C[t]==0:
                Q[rear], rear= t, rear+1
    print(dp[W])