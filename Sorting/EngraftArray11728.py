import sys
input= sys.stdin.readline

N, M= map(int,input().split())
A= list(map(int,input().split()))
B= list(map(int,input().split()))
S= []
for i in range(N):
    S.append(A[i])
for i in range(M):
    S.append(B[i])
S.sort()
S= map(str,S)
print(' '.join(S))