import heapq
import sys
input= sys.stdin.readline
Large= 1000000000
dir= [[-1,0],[1,0],[0,1],[0,-1]]

def Valid(r, c):
	if r<0 or r>=M:
		return False
	if c<0 or c>=N:
		return False
	return True

def DijkPq():
	pq, V, C= [], [], []
	for _ in range(M):
		V.append([False]*N)
		C.append([Large]*N)
	C[0][0]= A[0][0]
	heapq.heappush(pq, (C[0][0],0,0))
	while pq:
		co, r, c = heapq.heappop(pq)
		if V[r][c]==True:
			continue
		if r==M-1 and c==N-1:
			return co
		for i in range(4):
			nr, nc= r+dir[i][0], c+ dir[i][1]
			if (Valid(nr,nc)==False) or (V[nr][nc]==True):
				continue
			cc= C[r][c]+ A[nr][nc]
			if cc < C[nr][nc]:
				C[nr][nc]= cc
				heapq.heappush(pq, (C[nr][nc],nr,nc))	
	return -1
	
N, M= map(int,input().split())
A= []
for i in range(M):
    A.append(list(input().strip()))
    A[i]= list(map(int,A[i]))
print(DijkPq())