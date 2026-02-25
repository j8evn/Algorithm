import math
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
parent= [i for i in range(N)]
A= []
for i in range(N):
    A.append(list(map(int,input().split())))

M= int(input())
B= []
for _ in range(M):
    a, b= map(int, input().split())
    union_parent(a-1, b-1)
for a in range(N):
    for b in range(a+1, N):
        cost= math.sqrt((A[a][0]-A[b][0])**2 + (A[a][1]-A[b][1])**2)
        B.append((cost, a, b))
B.sort()

t= 0
cables= []
for cost, a, b in B:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        t += cost
        cables.append((a+1,b+1))
print(f"{t:.2f}")
for a, b in cables:
    print(a, b)