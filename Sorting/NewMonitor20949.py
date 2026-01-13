import sys
input= sys.stdin.readline

N= int(input())
A= []
for i in range(N):
    w, h= map(int,input().split())
    A.append([w*w+h*h,i+1])
A.sort(key=lambda x:-x[0])

for i in range(N):
    print(A[i][1])