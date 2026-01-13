from collections import deque
import sys
input= sys.stdin.readline

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
    while que:
        r, c= que.popleft()
        for i in range(4):
            nr, nc= r+dir[i][0], c+dir[i][1]
            if (Valid(nr,nc)==True) and (V[nr][nc]==False) and (A[nr][nc]!=0):
                V[nr][nc]= True
                que.append((nr,nc))
    return

dir= [[-1,0],[1,0],[0,-1],[0,1]]

N= int(input())
A= []
mm= -1
for i in range(N):
    A.append(list(map(int,input().split())))
    mm= max(mm,max(A[i]))

M= 0
for k in range(mm):
    for i in range(N):
        for j in range(N):
            if A[i][j]<=k:
                A[i][j]= 0
    V=[]
    for i in range(N):
        V.append([False]*N)

    cnt= 0
    for i in range(N):
        for j in range(N):
            if V[i][j]==False and A[i][j]!=0:
                bfs(i,j)
                cnt += 1
    M= max(M,cnt)
print(M)