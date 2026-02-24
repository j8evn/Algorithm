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

n, k= map(int, input().split())
parent= [i for i in range(n+1)]

ll= []
for _ in range(n):
    ll.append(input().rstrip())

A= []
for i in range(n):
    for j in range(i+1, n):
        cost= 0
        for a, b in zip(ll[i], ll[j]):
            cost += abs(ord(a)-ord(b))
        A.append((cost, i+1, j+1))
A.sort()

mm, cnt= 0, 0
for cost, a, b in A:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        mm= cost
        cnt += 1
        if cnt==n-1:
            break
print(mm)