import sys
input = sys.stdin.readline

def Comp(a, b):
	for i in range(K):
		if (a[i] != b[i]):
			return False
	return True

N = int(input())
A = []
for i in range(N):
	A.append(int(input()))
K = int(input())
C = []
for i in range(K):
	C.append(int(input()))

C.sort()
mm = min(C)
for i in range(K):
	C[i] = C[i]-mm

R= []

for i in range(N-K+1):
	P = A[i:i+K]
	P.sort()
	mm = min(P)
	for j in range(K):
		P[j] = P[j]-mm
	if (Comp(P,C)== True):
		R.append(i+1)
print(len(R))
R = list(map(str, R))
print('\n'.join(R))

