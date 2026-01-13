class BiMatch:
    def __init__(self, n, m, g):
        self.N, self.M, self.G = n, m, g
        self.A, self.B = [-1] * self.N, [-1] * self.M
        self.V = [False] * self.N

    def dfs(self, a):
        if self.V[a]:
            return False
        self.V[a] = True
        for b in self.G[a]:
            if self.B[b] == -1 or (not self.V[self.B[b]] and self.dfs(self.B[b])):
                self.A[a] = b
                self.B[b] = a
                return True
        return False

    def match(self):
        cnt = 0
        for i in range(self.N):
            self.V = [False] * self.N
            if self.dfs(i):
                cnt += 1
            self.V = [False] * self.N
            if self.dfs(i):
                cnt += 1
        return cnt

import sys
input = sys.stdin.readline

N = int(input())
shark = [list(map(int, input().split())) for _ in range(N)]

G = [[] for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        if shark[i][0] >= shark[j][0] and shark[i][1] >= shark[j][1] and shark[i][2] >= shark[j][2]:
            G[i].append(j)
        elif shark[i][0] <= shark[j][0] and shark[i][1] <= shark[j][1] and shark[i][2] <= shark[j][2]:
            G[j].append(i)

unmatched = N - BiMatch(N, N, G).match()
print(max(1, unmatched))
