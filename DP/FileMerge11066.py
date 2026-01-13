import sys
input= sys.stdin.readline
sys.setrecursionlimit(5000)

def Merge(f, t):
    if f==t:
        return 0, A[f]
    if dpcost[f][t]!=-1:
        return dpcost[f][t], dpsize[f][t]
    mm, ss= 100000000, 0
    for i in range(f, t):
        c1, s1= Merge(f, i)
        c2, s2= Merge(i+1, t)
        nn= c1+c2+s1+s2
        if nn<mm:
            mm, ss= nn, s1+s2
    dpcost[f][t], dpsize[f][t]= mm, ss
    return mm, ss
    
T= int(input())
for _ in range(T):
    K= int(input())
    A= list(map(int,input().split()))
    dpcost, dpsize= [], []
    for _ in range(K+1):
        dpcost.append([-1]*(K+1))
        dpsize.append([-1]*(K+1))
    cc, zz= Merge(0, K-1)
    print(cc)