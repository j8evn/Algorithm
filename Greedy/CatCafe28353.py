import sys
input= sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
r, cnt = N-1, 0
for i in range(N):
	while ((r >i) and (A[i]+A[r] >K)):
		r= r-1
	if (r <=i):
		break
	cnt = cnt+1
	r = r-1
print(cnt)
