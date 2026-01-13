import sys
input = sys.stdin.readline

N, M, D, S = map(int, input().split())
A, C = [], [0]*M
for i in range(N):
	A.append([-1]*M)

for i in range(D):
	n, m, t = map(int, input().split())
	n, m, t = n-1, m-1, t-1
	if (A[n][m] == -1):
		A[n][m] = t
		C[m] += 1
	else:
		A[n][m] = min(A[n][m], t)

R = [True] *M
for i in range(S):
	n, t = map(int, input().split())
	n, t = n-1, t-1
	U = [False]*M
	for j in range(M):
		if (A[n][j] == -1):
			continue
		if (A[n][j] < t):
			U[j] = True
	for j in range(M):
		R[j] = R[j] and U[j]

mm =0
for i in range(M):
	if (R[i]==True):
		mm = max(mm, C[i])
print(mm)
