import sys
input= sys.stdin.readline

T= int(input())
for i in range(T):
    ss= input().strip()
    p, t= 0, 0
    for j in range(len(ss)):
        if ss[j]=='O':
            p += 1
            t += p
        else:
            p= 0
    print(t)
