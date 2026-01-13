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