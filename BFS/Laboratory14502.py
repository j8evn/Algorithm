from collections import deque
import copy

def wall(cnt): # 백트래킹
    if cnt==3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if G[i][j]==0:
                G[i][j]= 1
                wall(cnt+1)
                G[i][j]= 0

def Valid(r,c):
    if r<0 or r>=N:
        return False
    if c<0 or c>=M:
        return False
    return True

def bfs():
    V= []
    for i in range(N):
        V.append([False]*M)
    que= deque()
    A= copy.deepcopy(G)
    for i in range(N):
        for j in range(M):
            if A[i][j]==2:
                que.append((i,j))
    while que:
        r, c= que.popleft()
        for i in range(4):
            nr, nc= r+dir[i][0], c+dir[i][1]
            if (Valid(nr,nc)==True) and (V[nr][nc]==False) and (A[nr][nc]==0):
                V[nr][nc]= True
                A[nr][nc]= 2
                que.append((nr,nc))
    global R
    cnt= 0
    for i in range(N):
        for j in range(M):
            if A[i][j]==0:
                cnt += 1
    R= max(R,cnt)

N, M= map(int,input().split())
G= []
for i in range(N):
    G.append(list(map(int,input().split())))

dir= [[-1,0],[1,0],[0,-1],[0,1]]

R= 0
wall(0)
print(R)