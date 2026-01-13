import sys
input= sys.stdin.readline

n= int(input())
ll= list(input().strip())
for i in range(n-1):
    s= list(input().strip())
    for j in range(len(s)):
        if s[j] != ll[j]:
            ll[j]= '?'
print(''.join(ll))
