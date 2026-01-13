from collections import deque

def Valid(r,c):
    if r<0 or r>=N:
        return False
    if c<0 or c>=M:
        return False
    return True

def bfs(r,c):
    que= deque()
    que.append((r,c))
    V[r][c]= True
    cnt= 1
    while que:
        r, c= que.popleft()
        for i in range(4):
            nr, nc= r+dir[i][0], c+dir[i][1]
            if (Valid(nr,nc)==True) and (V[nr][nc]==False) and (A[nr][nc]==1):
                V[nr][nc]= True
                que.append((nr,nc))
                cnt += 1
    return cnt

N, M= map(int,input().split())
A= []
for i in range(N):
    A.append(list(map(int,input().split())))

V= []
cnt= 0
for i in range(N):
    V.append([False]*M)

dir= [[-1,0],[1,0],[0,-1],[0,1]]

R= []
for i in range(N):
    for j in range(M):
        if V[i][j]==False and A[i][j]==1:
            R.append(bfs(i,j))
if R:
    print(len(R))
    print(max(R))
else:
    print(0)
    print(0)