import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**5)

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a= find_parent(a)
    b= find_parent(b)
    if a < b:
        parent[b]= a
    else:
        parent[a]= b

n, m= map(int, input().split())
parent= [i for i in range(n+1)]

A= []
for i in range(m):
    a, b, cost= map(int, input().split())
    A.append((cost, a, b, i+1))
A.sort()

R= []
for cost, a, b, i in A:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        R.append(i)
print(len(R))
print(*R, sep='\n')