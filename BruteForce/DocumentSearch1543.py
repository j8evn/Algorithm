import sys
input= sys.stdin.readline

S= input().rstrip()
search= input().rstrip()
cnt= 0
i= 0 
while i<len(S):
    if S[i:i+len(search)]==search:
        i += len(search)
        cnt += 1
    else:
        i += 1
print(cnt)