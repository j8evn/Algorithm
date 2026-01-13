import sys
input= sys.stdin.readline

n= int(input())
S= set()
for _ in range(n):
    s1, s2= input().split()
    if s2=='enter':
        S.add(s1)
    elif s2=='leave' and s1 in S:
        S.remove(s1)
S= list(S)
S.sort(reverse=True)
print('\n'.join(S))