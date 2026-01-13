import sys
input= sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(n):
    D.append(n)
    V[n]= True
    for e in G[n]:
        if V[e]== False:
            dfs(e)

N, M, R= map(int,input().split())
G= [[] for _ in range(N)]
V= [False]*N
for _ in range(M):
    u, v= map(int,input().split())
    u, v= u-1, v-1
    G[u].append(v)
    G[v].append(u)
for i in range(N):
    G[i].sort(reverse=True)

D= []
rr= [0]*N
dfs(R-1)
for i in range(len(D)):
    rr[D[i]]= i+1
rr= map(str,rr)
print('\n'.join(rr))