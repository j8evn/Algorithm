import sys
input=sys.stdin.readline

A, B= map(int,input().split())
P=[True]*(B+1)
for i in range(2,B+1):
    if P[i]==True:
        u=i*2
        while (u<=B):
            P[u]=False
            u=u+i

R =[]
A = max([2,A])
for i in range(A, B+1):
    if (P[i] ==True):
        R.append(i)
R = list(map(str, R))
print("\n".join(R))