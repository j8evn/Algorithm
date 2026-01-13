import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A =[]
for i in range(M):
	A.append(int(input()))
A.sort(reverse=True)
B = min(M, N)
mm, mi = -1, -1
for i in range(B):
	tt = (i+1)*A[i]
	if (tt > mm):
		mm, mi = tt, A[i]
print(mi, mm)