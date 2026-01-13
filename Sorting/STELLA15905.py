import sys
input= sys.stdin.readline

N= int(input())
A= []
for _ in range(N):
    A.append(list(map(int,input().split())))
A.sort(key=lambda x:x[1])
A.sort(key=lambda x:-x[0])

cnt= 0
i= 5
while i<N:
    if A[4][0]==A[i][0]:
        cnt += 1
    i+= 1
print(cnt)