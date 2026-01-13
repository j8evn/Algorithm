import sys
sys.setrecursionlimit(100000) 
'''
def dfs(n):
    global cnt
    if len(Tree[n])==0:
        cnt += 1
        return 
    for e in Tree[n]:
        dfs(e)
cnt= 0
'''
def dfs(n):
    if len(Tree[n])==0:
        return 1
    ss= 0
    for e in Tree[n]:
        ss += dfs(e)
    return ss

n= int(input())
Tree= []
for i in range(n):
    Tree.append([])
N= list(map(int,input().split()))
d= int(input())

for i in range(n):
    if N[i]==-1:
        r= i # 루트
    else:
        Tree[N[i]].append(i)

for i in range(n):
    if d in Tree[i]:
        Tree[i].remove(d)

if d==r:
    print(0)
else:
    print(dfs(r))