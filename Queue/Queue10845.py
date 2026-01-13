import sys
input= sys.stdin.readline

n= int(input())
que= []
for i in range(n):
    p= list(input().split())
    if p[0]=='push':
        que.append(int(p[1]))
    elif p[0]=='pop':
        if len(que)==0:
            print(-1)
        else:
            print(que.pop(0))
    elif p[0]=='size':
        print(len(que))
    elif p[0]=='empty':
        if len(que)==0:
            print(1)
        else:
            print(0)
    elif p[0]=='front':
        if len(que)==0:
            print(-1)
        else:
            print(que[0])
    elif p[0]=='back':
        if len(que)==0:
            print(-1)
        else:
            print(que[-1])