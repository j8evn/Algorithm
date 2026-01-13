def bfs(n):
    fr, re= 0, 0
    V[n]= True
    que[re], re= n, re+1
    while (fr!=re):
        nn, fr= que[fr], fr+1
        for e in G[nn]:
            if V[e]==True:
                continue
            V[e]= True
            que[re], re= e, re+1

N, M= map(int,input().split())
G= []

V=[False]*N
for i in range(N):
    G.append([])
for i in range(M):
    n1, n2= map(int,input().split())
    n1, n2= n1-1, n2-1
    G[n1].append(n2)
    G[n2].append(n1)

que=[-1]*(N+5)
cnt= 0
for i in range(N):
    if V[i]==False:
        bfs(i)
        cnt += 1
print(cnt)