T=int(input())
for i in range(T):
    N=int(input())
    S,L=[],[]
    for j in range(N):
        s,l=input().split()
        l=int(l)
        S.append(s)
        L.append(l)
    print(S[L.index(max(L))])
