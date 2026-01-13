from collections import deque

def Valid(r,c):
    if r<0 or r>=N:
        return False
    if c<0 or c>=N:
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
            if (Valid(nr,nc)==True) and (V[nr][nc]==False) and (A[nr][nc]=='1'):
                V[nr][nc]= True
                que.append((nr,nc))
                cnt += 1
    return cnt

N= int(input())
A= []
for i in range(N):
    A.append(input())

V= []
cnt= 0
for i in range(N):
    V.append([False]*N)

dir= [[-1,0],[1,0],[0,-1],[0,1]]

R= []
for i in range(N):
    for j in range(N):
        if V[i][j]==False and A[i][j]=='1':
            R.append(bfs(i,j))
print(len(R))
R.sort()
for e in R:
    print(e)