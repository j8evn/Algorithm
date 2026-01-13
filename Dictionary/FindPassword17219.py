import sys
input= sys.stdin.readline

N, M= map(int,input().split())
dic= {}
for _ in range(N):
    n, m= input().split()
    dic[n]= m

R= []
for _ in range(M):
    R.append(dic[input().strip()])
print('\n'.join(R))