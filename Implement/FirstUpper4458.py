import sys
input= sys.stdin.readline

N= int(input())
for _ in range(N):
    s= list(input().rstrip())
    s[0]= s[0].upper()
    print(''.join(s))