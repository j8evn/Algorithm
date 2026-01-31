import sys
input= sys.stdin.readline

s= input().rstrip()
cnt= 0
pre= 'A'
for i in range(len(s)):
    cnt += min(abs(ord(s[i])-ord(pre)), 26-abs(ord(s[i])-ord(pre)))
    pre= s[i]
print(cnt)