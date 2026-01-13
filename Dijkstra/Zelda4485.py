# 백준 4485
# ICPC Regionals :2008 Pacific Northwest Region Programming Contest D번
# 격자에서의 다익스트라 - 각 격자가 노드, 상하좌우가 연결 링크
# 범위를 벗어나는지 체크하는 부분 필요

import heapq
import sys
input= sys.stdin.readline
Large= 1000000000
dir= [[-1,0],[1,0],[0,1],[0,-1]]

def Valid(r, c):
	if r<0 or r>=N:
		return False
	if c<0 or c>=N:
		return False
	return True

def DijkPq():
	pq, V, C= [], [], []
	for _ in range(N):
		V.append([False]*N)
		C.append([Large]*N)
	C[0][0]= A[0][0]
	heapq.heappush(pq, (C[0][0],0,0))
	while pq:
		co, r, c = heapq.heappop(pq)
		if V[r][c]==True:
			continue
		if r==N-1 and c==N-1:
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
	
R, idx= [], 1
while True:
	N= int(input())
	if (N==0):
		break
	A= []
	for _ in range(N):
		A.append(list(map(int, input().split())))
	R.append("Problem "+str(idx)+": " + str(DijkPq()))
	idx += 1
print("\n".join(R))