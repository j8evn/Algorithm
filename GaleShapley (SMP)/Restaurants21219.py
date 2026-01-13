import sys
import heapq
input = sys.stdin.readline

class Boy:
    def __init__(self, p):
        self.pos = 0
        self.pref = p
    def dump(self):
        print(self.pos, self.pref)

class Girl:
    def __init__(self, p, cc):
        self.pref = {cust: rank for rank, cust in enumerate(p)}
        self.capa = cc
        self.match = []

    def fight(self, a):
        heapq.heappush(self.match, (-self.pref.get(a, float('inf')), a))
        if len(self.match) > self.capa:
            _, removed = heapq.heappop(self.match)
            return removed
        return -1

    def dump(self):
        print([b for _, b in self.match], self.pref)

N, M = map(int, input().split())
C = []
for _ in range(M):
    C.append(int(input()))

B = []
for _ in range(N):
    tt = list(map(int, input().split()))
    for j in range(len(tt)):
        tt[j] -= 1
    B.append(Boy(tt))

G = []
for i in range(M):
    tt = list(map(int, input().split()))
    for j in range(len(tt)):
        tt[j] -= 1
    G.append(Girl(tt, C[i]))

unmatched = set(range(N))

while unmatched:
    chal = unmatched.pop()
    cur = B[chal]
    
    while cur.pos < len(cur.pref):
        tar = cur.pref[cur.pos]
        cur.pos += 1
        
        removed = G[tar].fight(chal)
        
        if removed != -1:
            unmatched.add(removed)
        break

result = sorted(cust for rest in G for _, cust in rest.match)
print(*[r + 1 for r in result], sep='\n')
