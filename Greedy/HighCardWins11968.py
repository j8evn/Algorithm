import sys
input = sys.stdin.readline

def FindFrom(n):
	for i in range(n, 2*N):
		if (A[i] == True):
			return i
	return -1

N = int(input())
P =[]
A = [True]* (2*N)
for i in range(N):
	e = int(input())-1
	P.append(e)
	A[e] = False

cnt = 0
for i in range(N):
	t = FindFrom(P[i])
	if (t != -1):
		cnt +=1
		A[t] = False
	else:
		t = FindFrom(0)
		A[t]= False

print(cnt)