class BiMatch:
	def __init__(self, n, m, g):
		self.N, self.M, self.G= n, m, g
		self.A, self.B= [-1]*self.N, [-1]*self.M
		self.V= [False]*self.N

	def dfs(self, a) :
		if (self.V[a]==True):
			return False
		self.V[a]= True
		see= self.G[a]
		for b in see:
			if ((self.B[b]==-1) or ((self.V[self.B[b]]==False) and (self.dfs(self.B[b])))) :
				self.A[a]= b
				self.B[b]= a
				return True
		return False

	def match(self) :
		self.A, self.B= [-1]*self.N, [-1]*self.M
		cnt= 0
		for i in range(self.N):
			self.V= [False]*self.N
			if (self.dfs(i)==True):
				cnt += 1
		return cnt

import math
import sys
input= sys.stdin.readline

while True:
    line = input()
    if not line:
        break
    N, M, S, V= map(int,line.split())
    G= [[] for _ in range(N)]

    t1, t2= [], []
    for _ in range(N):
        x, y= map(float,input().split())
        t1.append([x,y])
    for _ in range(M):
        x, y= map(float,input().split())
        t2.append([x,y])

    for i in range(N):
        for j in range(M):
            if S*V >= math.sqrt((t1[i][0]-t2[j][0])**2+(t1[i][1]-t2[j][1])**2):
                G[i].append(j)

    print(N-BiMatch(N,M,G).match())