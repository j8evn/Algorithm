import sys
input= sys.stdin.readline

T= int(input())
for _ in range(T):
    n= int(input())
    t= list(map(int,input().split()))
    C, G= [0]*n, [[] for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1,n):
            G[t[i]-1].append(t[j]-1)
            C[t[j]-1]= C[t[j]-1]+1
    m= int(input())
    ck= []
    for _ in range(m):
        a, b= map(int,input().split())
        ai= t.index(a-1)
        bi= t.index(b-1)
        ck.append(ai-bi)
        t[ai], t[bi]= t[bi], t[ai]
    print(G)
    print(ck)
'''
    if flag== false
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
    '''