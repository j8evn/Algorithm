import sys
input= sys.stdin.readline

class Boy:
	def __init__(self, p):
		self.pos = 0
		self.pref = p
	def dump(self):
		print(self.pos, self.pref)

class Girl:
	def __init__(self, id):
		self.id = id
		self.match = -1
  
	def fight(self, a):
		if (self.match == -1):
			self.match = a
			return -1
		else:
			c = self.match
			l1 = abs(self.id - c)
			l2 = abs(self.id - a)
			if (l1 > l2):
				return a
			elif (l1 < l2):
				self.match = a
				return c
			else:
				if (c <a):
					return a
				else:
					self.match = a
					return c
	def dump(self):
		print(self.match, self.pref)

N= int(input())
B= []
for i in range(N):
	tt= list(map(int, input().split()))
	for j in range(len(tt)):
		tt[j] -= 1
	B.append(Boy(tt))
G= []
for i in range(N):
	G.append(Girl(i))

'''
for i in range(N):
	B[i].dump()
'''

for i in range(N):
	chal= i
	while (chal != -1):
		cur= B[chal]
		if (cur.pos >= len(cur.pref)):
			break
		tar= cur.pref[cur.pos]
		cur.pos += 1
		if (G[tar].match == -1):
			G[tar].match = chal
			break
		chal= G[tar].fight(chal)
		cur= B[chal]

R= [-1]*N
for i in range(N):
	b= G[i].match
	R[b]= i+1
R= list(map(str, R))
print(" ".join(R))