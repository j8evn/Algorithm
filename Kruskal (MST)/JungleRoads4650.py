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

while True:
    N= int(input())
    if N==0:
        break
    parent= [i for i in range(N+1)]

    A= []
    for _ in range(N-1):
        ll= list(input().split())
        for i in range(2,len(ll),2):
            cost= int(ll[i+1])
            a= ord(ll[0])-ord('A')
            b= ord(ll[i])-ord('A')
            A.append((cost, a, b))
    A.sort()

    t= 0
    for cost, a, b in A:
        if find_parent(a) != find_parent(b):
            union_parent(a, b)
            t += cost
    print(t)