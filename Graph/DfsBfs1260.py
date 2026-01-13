from collections import deque

def dfs(n): # 깊이 우선 탐색: 재귀호출 사용
    D.append(n+1)
    V1[n]= True # 시작 노드 방문 처리
    for e in G[n]:
        if V1[e]== False:
            dfs(e) # 인접한 노드 중 방문하지 않은 노드로 방문

def bfs(n): # 너비 우선 탐색: 큐 사용
    que= deque()
    que.append(n)
    V2[n]= True
    while que: # 큐가 비어있지 않은 동안
        nn= que.popleft()
        B.append(nn+1)
        for e in G[nn]:
            if V2[e]==False: # 인접한 노드 중 방문하지 않은 노드로 방문
                V2[e]= True
                que.append(e)

N, M, R= map(int,input().split())
R= R-1
V1= [False]*N # DFS의 방문 여부
V2= [False]*N # BFS의 방문 여부

G= [] # 그래프 만들기
for i in range(N):
    G.append([])
for i in range(M):
    n1, n2= map(int,input().split())
    n1, n2= n1-1, n2-1
    G[n1].append(n2)
    G[n2].append(n1)

# 정점 번호가 작은 것부터 방문하기 위해 오름차순 정렬
for i in range(N):
    G[i].sort() 

D= [] # dfs 결과
dfs(R)
D= map(str,D)
print(' '.join(D))

B= [] # bfs 결과
bfs(R)
B= map(str,B)
print(' '.join(B))