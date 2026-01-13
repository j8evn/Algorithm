import sys
input= sys.stdin.readline

n= int(input())
A= []
for _ in range(n):
	A.append(list(map(int,input().split())))
A.sort(key=lambda x:x[0])
A.sort(key=lambda x:x[1])

cnt = 1
r= A[0][1]
for i in range(1,n):
	if r<=A[i][0]:
		cnt += 1
		r= A[i][1]
print(cnt)