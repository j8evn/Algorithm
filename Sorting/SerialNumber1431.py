import sys
input= sys.stdin.readline

N= int(input())
S= []
for _ in range(N):
    s= input().strip()
    t= 0
    for i in range(len(s)):
        if ord('0') <= ord(s[i]) <= ord('9'):
            t += int(s[i])
    S.append([len(s), t, s])
S.sort(key= lambda x: (x[0], x[1], x[2]))

print("\n".join([s[2] for s in S]))