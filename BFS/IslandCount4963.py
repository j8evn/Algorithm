def Valid(r,c):
    if r<0 or r>=M:
        return False
    if c<0 or c>=N:
        return False
    return True

def bfs(r,c):
    que, fr= [], 0
    que.append([r,c])
    V[r][c]= True
    while (len(que)>fr):
        r, c= que[fr][0], que[fr][1]
        fr += 1
        for i in range(8):
            nr, nc= r+dir[i][0], c+dir[i][1]
            if (Valid(nr,nc)==True) and (V[nr][nc]==False) and (A[nr][nc]==1):
                V[nr][nc]= True
                que.append([nr,nc])
    return

while True:
    N, M= map(int,input().split())
    if M==0 and N==0:
        break
    A= []
    for i in range(M):
        A.append(list(map(int,input().split())))

    V=[] # 방문 여부
    for i in range(M):
        V.append([False]*N)

    dir= [[-1,0],[1,0],[0,-1],[0,1],[-1,1],[1,1],[-1,-1],[1,-1]] # 왼쪽, 오른쪽, 아래, 위

    cnt= 0
    for i in range(M):
        for j in range(N):
            if V[i][j]==False and A[i][j]==1:
                bfs(i,j)
                cnt += 1
    print(cnt)