import sys
input= sys.stdin.readline

N= int(input())
A= []
for _ in range(N):
    A.append(list(map(int,input().split())))
A.sort(key=lambda x:x[1])
A.sort(key=lambda x:x[0])

ss= 0
for i in range(N):
    ss += (A[i][0]*(i+1)+A[i][1])
print(ss)