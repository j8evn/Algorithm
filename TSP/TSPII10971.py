import sys
input= sys.stdin.readline

def Perm(n):
    global d
    if (n==N):
        cur = Eval()
        d = min(d,cur)
        #print(cur)
    for i in range(N):
        if (V[i]==False):
            V[i] = True
            A[n] = i
            Perm(n+1)
            V[i] = False

def Eval():
    #print(A)
    ss = 0
    for i in range(len(A)):
        ss += cost[A[i]][A[(i+1)%N]]
    return ss

d= 10000000
N= int(input())
cost= []
for i in range(N):
    cost.append(list(map(int,input().split())))
    for j in range(len(cost[i])):
        if cost[i][j]==0:
            cost[i][j]=1000000000
V, A = [False]*N, [-1]*N
V[0], A[0] = True, 0
Perm(1)
print(d)