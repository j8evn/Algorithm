def CopyMat(A, B):
	for i in range(N):
		for j in range(N):
			B[i][j] = A[i][j]

def MulMat(A, B, C):
	for i in range(N):
		for j in range(N):
			ss =0
			for k in range(N):
				ss += A[i][k]*B[k][j]
				ss = ss % 31991
			C[i][j] = ss

N, s = map(int, input().split())
F, E, C = [], [], []
for i in range(N):
	F.append([0]*N)
	E.append([0]*N)
	C.append([0]*N)
for i in range(N):
	F[i][i] = 1
	E[0][i] =1
for i in range(1, N):
	E[i][i-1] =1

while (s !=0):
	if (s %2 ==1):
		MulMat(F, E, C)
		CopyMat(C, F)
	s = s//2
	MulMat(E, E, C)
	CopyMat(C, E)
#	print(E, F)
print (F[0][0])
