## 핵심 로직: 먹을 수 있는 물고기가 없을 때까지 최단 거리 탐색을 반복
# size로 길을 찾고(BFS), 발견된 후보들을 fish_list에 모아 정렬한 뒤, 가장 좋은 후보의 거리만큼 t에 더하고 shark_idx*를 옮기는 과정을 반복

from collections import deque
import sys
input= sys.stdin.readline

def Valid(r,c):
    if r<0 or r>=N:
        return False
    if c<0 or c>=N:
        return False
    return True

def bfs(sr, sc, size):
    que= deque([(sr, sc, 0)])
    V= [[False]*N for _ in range(N)]
    V[sr][sc]= True
    fish_list= []
    mm= 10000000000 # 지금까지 찾은 물고기 중 최단거리 (효율성 위함, 없어도 문제 없음)
    while que:
        r, c, d= que.popleft()
        if d >= mm: # 현재 거리가 이미 찾은 물고기 거리보다 더 멀면 break (효율적)
            continue
        for i in range(4):
            nr, nc= r+dir[i][0], c+dir[i][1]
            if (Valid(nr,nc)==True) and (V[nr][nc]==False) and (A[nr][nc] <= size):
                V[nr][nc]= True
                if 0 < A[nr][nc] < size: # 0보다 크고 상어보다 작은 물고기 list에 추가
                    fish_list.append((d+1,nr,nc))
                    mm= d+1
                else: # 빈칸이거나 크기가 같은 물고기인 경우 지나만 감
                    que.append((nr,nc,d+1))
    if not fish_list:
        return None
    
    fish_list.sort() # 거리->위->왼 순으로 정렬
    return fish_list[0]

N= int(input())
A= []
for _ in range(N):
    A.append(list(map(int,input().split())))

dir= [[-1,0],[1,0],[0,-1],[0,1]]

que= deque()
for i in range(N):
    for j in range(N):
        if A[i][j] == 9:
            shark_idx= (i,j)
            A[i][j]= 0

size= 2 # 상어의 처음 크기
cnt, t= 0, 0 # 먹은 물고기 수, 총 걸린 시간

while True: # 상어의 위치에서 bfs 반복
    res= bfs(shark_idx[0], shark_idx[1], size)
    if res is None:
        break
    d, nr, nc= res
    
    t += d
    shark_idx= (nr, nc)
    A[nr][nc]= 0
    cnt += 1
    
    if cnt == size:
        size += 1
        cnt= 0

print(t)