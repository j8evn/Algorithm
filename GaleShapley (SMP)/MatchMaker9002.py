# 백준 9002
# ICPC Regionals: Korea Asia Regional Taejon 2000 E번
# SMP인데... 예제 답에서 일반적인 Gale-Shapley랑 다른 답을 보여줌
# Stable한 매칭의 답이 여러 개 있을 수 있고 Gale-Shapley는 그중에 하나를 찾아줄 수 있는 알고리즘이라고 한다.

import sys
input = sys.stdin.readline

class Boy:
	def __init__(self, p):
		self.pos = 0
		self.pref = p
	def dump(self):
		print(self.pos, self.pref)

class Girl:
	def __init__(self, p):
		self.match = -1
		self.pref = p

# returns loser (next challenger)
	def fight(self, a):
		if (self.match == -1):
			self.match = a
			return -1
		else:
			c = self.match
			for i in range(N):
				if (self.pref[i] == a):
					self.match = a
					return c
				elif (self.pref[i] == c):
					self.match == c
					return a
		return -1
	def dump(self):
		print(self.match, self.pref)

def Proc():
	for i in range(N):
		chal = i
		while (chal != -1):
			cur = B[chal]
			if (cur.pos >= len(cur.pref)):
				break
			tar = cur.pref[cur.pos]
			cur.pos += 1
			if (G[tar].match == -1):
				G[tar].match = chal
				break
			chal = G[tar].fight(chal)
			cur= B[chal]

	R= [-1]*N
	for i in range(N):
		b = G[i].match
		R[b] = i+1
	R = list(map(str, R))
	return(" ".join(R))

import sys
input = sys.stdin.readline
ans =[]
T = int(input())
for t in range(T):
	N = int(input())
	B=[]
	for i in range(N):
		tt = list(map(int, input().split()))
		for j in range(N):
			tt[j] -=1
		B.append(Boy(tt))
	G =[]
	for i in range(N):
		tt = list(map(int, input().split()))
		for j in range(N):
			tt[j] -=1
		G.append(Girl(tt))
	ans.append(Proc())
print("\n".join(ans))