import sys
input= sys.stdin.readline

while True:
    N, M= map(int,input().split())
    if N==0 and M==0:
        break
    C, G= [0]*N, [[] for _ in range(N)]
    for _ in range(M):
        n1, n2= map(int,input().split())
        n1, n2= n1-1, n2-1
        G[n1].append(n2)
        C[n2]= C[n2]+1
        
    Q, front, rear= [0]*N, 0, 0
    for i in range(N):
        if C[i]==0:
            Q[rear], rear= i, rear+1

    R= []
    while front<rear:
        n, front= Q[front], front+1
        R.append(n+1)
        for t in G[n]:
            C[t]= C[t]-1
            if C[t]==0:
                Q[rear], rear= t, rear+1
    if len(R)==N:
        R= map(str,R)
        print('\n'.join(R))
    else:
        print("IMPOSSIBLE")