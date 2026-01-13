import sys
sys.setrecursionlimit(10000)
input= sys.stdin.readline

def dfs(n,d):
    if d==5:
        print(1)
        exit()
    V[n]= True
    for e in G[n]:
        if V[e]== False:
            dfs(e,d+1)
            V[e]= False

N, M= map(int,input().split())
G= [[] for _ in range(N)]
for _ in range(M):
    a, b= map(int,input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(N):
    V= [False]*N
    dfs(i,1)
print(0)