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
					self.match = c
					return a
		return -1
	def dump(self):
		print(self.match, self.pref)

N = int(input())

B=[]
for i in range(N):
	tt = list(map(int, input().split()))
	for j in range(N):
		tt[j] -=1 # 인덱스 처리
	B.append(Boy(tt))
G =[]
for i in range(N):
	tt = list(map(int, input().split()))
	for j in range(N):
		tt[j] -=1
	G.append(Girl(tt))

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
print("\n".join(R))