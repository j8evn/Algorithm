def Valid(r,c):
    if r<0 or r>=N:
        return False
    if c<0 or c>=N:
        return False
    return True

def bfs(r,c,x,y):
    que, fr= [], 0
    que.append([r,c])
    while (len(que)>fr):
        r, c= que[fr][0], que[fr][1]
        if r==x and c==y:
            return V[r][c]
        fr += 1
        for i in range(8):
            nr, nc= r+dir[i][0], c+dir[i][1]
            if (Valid(nr,nc)==True) and V[nr][nc]==0:
                V[nr][nc]= V[r][c]+1
                que.append([nr,nc])

dir= [[-2,1],[-1,2],[2,1],[1,2],[-2,-1],[-1,-2],[2,-1],[1,-2]]

T= int(input())
for _ in range(T):
    N= int(input())
    a, b= map(int,input().split())
    x, y= map(int,input().split())
    V= [[0]*N for _ in range(N)]
    print(bfs(a,b,x,y))