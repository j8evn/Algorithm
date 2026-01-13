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

import sys
input= sys.stdin.readline

N, M= map(int,input().split())
w1, w2= [], []
for _ in range(N):
    w1.append(int(input()))
for _ in range(M):
    w2.append(int(input()))

G= [[] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if w1[i]/2<=w2[j]<=w1[i]*(3/4) or w1[i]<=w2[j]<=w1[i]*(5/4):
            G[i].append(j)

print(BiMatch(N,M,G).match())