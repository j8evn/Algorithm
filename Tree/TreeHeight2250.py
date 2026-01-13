import sys
sys.setrecursionlimit(100000) 

def inorder(n): # 각 노드의 번호
    global idx
    if n==-2:
        return
    inorder(Tree[n][0])
    L[n]= idx
    idx += 1
    inorder(Tree[n][1])

def dfs(n,d): # 각 노드의 레벨
    D[n]= d
    if Tree[n][0]!=-2:
        dfs(Tree[n][0],d+1)
    if Tree[n][1]!=-2:
        dfs(Tree[n][1],d+1)

N= int(input())
Tree= []
V= [True]*N
L, D= [-1]*N, [-1]*N
idx= 0
for i in range(N):
    Tree.append([0,0])
for i in range(N):
    n1, n2, n3= map(int,input().split())
    if n2!=-1:
        V[n2-1]= False
    if n3!=-1:
        V[n3-1]= False
    Tree[n1-1][0]= n2-1
    Tree[n1-1][1]= n3-1

r= V.index(True)
inorder(r)
dfs(r,1)
m= [[] for _ in range(max(D)+1)]
for i in range(N):
    m[D[i]].append(L[i])
res= []
for i in range(len(m)):
    if len(m[i])<=1:
        res.append(1)
    else:
        res.append(max(m[i])-min(m[i])+1)
print(res.index(max(res),1), max(res))