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
G= [[] for _ in range(N)]
g= list(map(int,input().split()))
b= list(map(int,input().split()))
l= list(map(int,input().split()))
u= list(map(int,input().split()))
for i in range(N):
    for j in range(M):
        if b[j]<l[i] and g[i]>u[j]:
            G[i].append(j)
print(BiMatch(N,M,G).match())