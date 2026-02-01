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

N= int(input())
M= int(input())
parent= [i for i in range(N+1)]

A= []
for _ in range(M):
    a, b, cost= map(int, input().split())
    A.append((cost, a, b))
A.sort()

t= 0
for cost, a, b in A:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        t += cost
print(t)