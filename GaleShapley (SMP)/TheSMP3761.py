import sys
input = sys.stdin.readline

class Boy:
	def __init__(self, p):
		self.pos = 0
		self.pref = p

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

T= int(input())
for _ in range(T):
    N = int(input())
    A= list(input().split())
    bb= A[:N]
    bdic= {}
    for i in range(N):
        bdic[bb[i]]= i
    gg= A[N:]
    gdic= {}
    for i in range(N):
        gdic[gg[i]]= i

    t1, t2= [[] for _ in range(N)], [[] for _ in range(N)]
    for i in range(N):
        tt = input().strip()
        for j in range(2,len(tt)):
            t1[bdic[tt[0]]].append(gdic[tt[j]])
    for i in range(N):
        tt = input().strip()
        for j in range(2,len(tt)):
            t2[gdic[tt[0]]].append(bdic[tt[j]])

    B= []
    for i in range(N):
        B.append(Boy(t1[i]))
    G= []
    for i in range(N):
        G.append(Girl(t2[i]))

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
        R[b] = i
    
    ans= []
    bdic= {value:key for key,value in bdic.items()}
    gdic= {value:key for key,value in gdic.items()}
    for i in range(N):
        ans.append([bdic[i],gdic[R[i]]])
    ans.sort(key=lambda x:x[0])
    for i in range(N):
        print(' '.join(ans[i]))
    print()