# 2차원 list는 list of list: list의 원소가 list임
# A[i][j] : i번째 행(row)에 j번째 열(column)

M, N = map(int, input().split())
A, B =[], []
# A, B에 append될 게 또 list임
for i in range(M):
	A.append(list(map(int, input().split())))
for i in range(M):
	B.append(list(map(int, input().split())))

for i in range(M):
	for j in range(N):
		A[i][j] = A[i][j]+B[i][j]
for i in range(M):
	tt = map(str, A[i])
	print(' '.join(tt))
