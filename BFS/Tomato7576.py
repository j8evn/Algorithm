from collections import deque

def Valid(r,c):
    if r<0 or r>=M:
        return False
    if c<0 or c>=N:
        return False
    return True

def bfs():
    cnt= 0
    while que:
        ll= len(que)
        cnt += 1
        for _ in range(ll):
            r, c= que.popleft()
            for i in range(4):
                nr, nc= r+dir[i][0], c+dir[i][1]
                if (Valid(nr,nc)==True) and (V[nr][nc]==False) and (A[nr][nc]==0):
                    V[nr][nc]= True
                    A[nr][nc]= 1
                    que.append((nr,nc))
    return cnt

N, M= map(int,input().split())
A= []
for _ in range(M):
    A.append(list(map(int,input().split())))
V= []
for i in range(M):
    V.append([False]*N)

dir= [[-1,0],[1,0],[0,-1],[0,1]]

que= deque()
for i in range(M):
    for j in range(N):
        if A[i][j]==1:
            que.append((i,j))
            V[i][j]= True
R= bfs()
Check= True
for i in range(M):
    for j in range(N):
        if A[i][j]==0:
            Check= False
if Check==True:
    print(R-1)
else:
    print(-1)
