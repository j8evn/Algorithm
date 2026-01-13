class BiMatch:
    def __init__(self, n, m, g):
        self.N, self.M, self.G= n, m, g
        self.A, self.B= [-1]*self.N, [-1]*self.M
        self.V= [False]*self.N

    def dfs(self, a):
        if (self.V[a]==True):
            return False
        self.V[a]= True
        see= self.G[a]
        for b in see:
            if self.B[b]==0: 
                continue
            if ((self.B[b]==-1) or ((self.V[self.B[b]]==False) and (self.dfs(self.B[b])))) :
                self.A[a]= b
                self.B[b]= a
                return True
        return False

    def match(self) :
        for g in range(len(self.G[0])):
            cnt= 1
            self.A, self.B= [-1]*self.N, [-1]*self.M
            self.A[0]= self.G[0][g]
            self.B[self.G[0][g]]= 0
            for i in range(1,self.N):
                self.V= [False]*self.N
                if (self.dfs(i)==True):
                    cnt += 1
            if cnt==self.N:
                R.append(tt[self.G[0][g]])

import sys
input= sys.stdin.readline

P = [True]*2001
for i in range(2,2001): 
    if (P[i] == True):
        u= i*2
        while (u<=2000):
            P[u] = False
            u= u+i

N= int(input())
tt= list(map(int,input().split()))
G= [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i!=j and P[tt[i]+tt[j]]==True:
            G[i].append(j)

R= []
BiMatch(N,N,G).match()
if R:
    R.sort()
    R= map(str,R)
    print(' '.join(R))
else:
    print(-1)