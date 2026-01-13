class BiMatch:
    def __init__(self, n, m, g):
        self.N, self.M, self.G = n, m, g
        self.A = [-1] * self.N
        self.B = [-1] * self.M
        self.visited = [False] * self.N

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
                cnt += 2
        return cnt


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    if (x+y)%2:
        if x%2:
            graph[x-1].append(y-1)
        else:
            graph[y-1].append(x-1)

b = BiMatch(n, n, graph)
res = b.match()

if res!=n:
    res += 1
print(res)
