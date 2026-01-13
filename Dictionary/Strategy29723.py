import sys
input= sys.stdin.readline

N, M, K= map(int,input().split())
dic= {}
for _ in range(N):
    s, p= input().split()
    p= int(p)
    dic[s]= p

mn, mx= 0, 0
for _ in range(K):
    t= input().strip()
    mn += dic[t]
    mx += dic[t]
    del dic[t]

ll= list(dic.values())
ll.sort()
for i in range(M-K):
    mn += ll[i]
    mx += ll[len(ll)-i-1]
print(mn, mx)