import sys
input= sys.stdin.readline

N= int(input())
S= []
for _ in range(N):
    S.append(int(input()))
S.sort(reverse=True)
S= map(str,S)
print('\n'.join(S))