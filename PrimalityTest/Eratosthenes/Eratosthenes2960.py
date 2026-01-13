import sys
input=sys.stdin.readline

cnt=0
N,K=map(int,input().split())
P=[True]*(N+1)
for i in range(2,N+1):
    if P[i]==True:
        u=i
        while (u<=N):
            if (P[u]==True):
                cnt+=1
                if (cnt==K):
                    print(u)
                    break
            P[u]=False
            u=u+i
