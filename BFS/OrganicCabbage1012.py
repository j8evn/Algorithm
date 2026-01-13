import sys
input= sys.stdin.readline

def Valid(r,c):
    if r<0 or r>=N:
        return False
    if c<0 or c>=M:
        return False
    return True

def bfs(r,c):
    que, fr= [], 0
    que.append([r,c])
    V[r][c]= True
    while (len(que)>fr):
        r, c= que[fr][0], que[fr][1]
        fr += 1
        for i in range(4):
            nr, nc= r+dir[i][0], c+dir[i][1]
            if (Valid(nr,nc)==True) and (V[nr][nc]==False) and (A[nr][nc]==1):
                V[nr][nc]= True
                que.append([nr,nc])
    return

dir= [[-1,0],[1,0],[0,-1],[0,1]]

T= int(input())
for _ in range(T):
    M, N, K= map(int,input().split())
    A= []
    for _ in range(N):
        A.append([0]*M)
    for _ in range(K):
        x, y= map(int,input().split())
        A[y][x]= 1
    V= []
    for _ in range(N):
        V.append([False]*M)
        
    cnt= 0
    for i in range(N):
        for j in range(M):
            if V[i][j]==False and A[i][j]==1:
                bfs(i,j)
                cnt += 1
    print(cnt)