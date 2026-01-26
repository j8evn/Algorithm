import sys
input= sys.stdin.readline

while True:
    n= int(input())
    if n==0:
        break
    s= input().strip()
    mm= 0
    for i in range(n-1, 0, -1):
        if s[:i]==s[n-i:]:
            mm= i
            break
    print(s+s[mm:])