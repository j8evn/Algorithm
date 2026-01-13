from collections import deque
import copy
import sys
input= sys.stdin.readline

def Valid(r,c):
    if r<0 or r>=N:
        return False
    if c<0 or c>=N:
        return False
    return True

def bfs(A,V,r,c):
    que= deque()
    que.append((r,c))
    V[r][c]= True
    while que:
        r, c= que.popleft()
        for i in range(4):
            nr, nc= r+dir[i][0], c+dir[i][1]
            if (Valid(nr,nc)==True) and (V[nr][nc]==False) and (A[r][c]==A[nr][nc]):
                V[nr][nc]= True
                que.append((nr,nc))

dir= [[-1,0],[1,0],[0,-1],[0,1]]

N= int(input())
G1= []
for i in range(N):
    G1.append(list(input().strip()))
G2= copy.deepcopy(G1)
for i in range(N):
    for j in range(len(G1[i])):
        if G1[i][j]=="R":
            G2[i][j]= "G"
V1, V2= [], []
for _ in range(N):
    V1.append([False]*N)
    V2.append([False]*N)

cnt1, cnt2= 0, 0
for i in range(N):
    for j in range(N):
        if V1[i][j]==False:
            bfs(G1,V1,i,j)
            cnt1 += 1
        if V2[i][j]==False:
            bfs(G2,V2,i,j)
            cnt2 += 1
print(cnt1,cnt2)