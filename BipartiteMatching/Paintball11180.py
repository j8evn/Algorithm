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
        global R
        self.A, self.B= [-1]*self.N, [-1]*self.M
        cnt= 0
        for i in range(self.N):
            self.V= [False]*self.N
            if (self.dfs(i)==True):
                cnt += 1
        R= copy.deepcopy(self.B)
        return cnt

import copy
import sys
input= sys.stdin.readline

N, M= map(int,input().split())
G= [[] for _ in range(N)]
for i in range(M):
    a, b= map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

R= []
B= BiMatch(N,N,G).match()
if B==N:
    for i in range(N):
        R[i] += 1
    R= map(str,R)
    print('\n'.join(R))
else:
    print("Impossible")