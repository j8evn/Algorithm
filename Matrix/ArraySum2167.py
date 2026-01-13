# 부분 배열도 각 행과 열이 일정해야 함

import sys
input= sys.stdin.readline

n, m= map(int,input().split())
A=[]
for a in range(n):
    A.append(list(map(int,input().split())))
k= int(input())
for a in range(k):
    i, j, x, y= map(int,input().split())
    i, j, x, y= i-1, j-1, x-1, y-1
    ss= 0
    for b in range(i,x+1):
        for c in range(j,y+1):
            ss += A[b][c]
    print(ss)

'''
n, m= map(int,input().split())
A=[]
for i in range(n):
    t = list(map(int,input().split()))
    for j in range (1,m):
        t[j] = t[j-1]+t[j]
    t.insert(0,0)
    A.append(t)
print(A)
k = int(input())
for i in range(k):
    r1, c1, r2, c2= map(int,input().split())
    r1, c1, r2, c2= r1-1, c1-1, r2-1, c2-1
    ss= 0
    for r in range(r1,r2+1):
        ss += A[r][c2+1]-A[r][c1]
        print(r, c2+1, r, c1)
    print(ss)
'''
