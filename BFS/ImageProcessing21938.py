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
    cnt= 1
    while (len(que)>fr):
        r, c= que[fr][0], que[fr][1]
        fr += 1
        for i in range(4):
            nr, nc= r+dir[i][0], c+dir[i][1]
            if (Valid(nr,nc)==True) and (V[nr][nc]==False) and (A[nr][nc]==255):
                V[nr][nc]= True
                que.append([nr,nc])
                cnt += 1
    return cnt

M, N= map(int,input().split())
A= []
for i in range(M):
    K= []
    tt= list(map(int,input().split()))
    for j in range(0,len(tt)-1,3):
        K.append((tt[j]+tt[j+1]+tt[j+2])/3)
    A.append(K)

T= int(input())
for i in range(M):
    for j in range(N):
        if A[i][j]>=T:
            A[i][j]= 255
        else:
            A[i][j]= 0

V=[]
for i in range(M):
    V.append([False]*N)

dir= [[-1,0],[1,0],[0,-1],[0,1]]

R= []
for i in range(M):
    for j in range(N):
        if V[i][j]==False and A[i][j]==255:
            R.append(bfs(i,j))
print(len(R))