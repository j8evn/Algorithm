import sys
input= sys.stdin.readline

M= int(input())
S= set()
for _ in range(M):
    k= list(input().split())
    if k[0]=="add":
        S.add(int(k[1]))
    elif k[0]=="remove":
        if int(k[1]) in S:
            S.remove(int(k[1]))
    elif k[0]=="check":
        if int(k[1]) in S:
            print(1)
        else:
            print(0)
    elif k[0]=="toggle":
        if int(k[1]) in S:
            S.remove(int(k[1]))
        else:
            S.add(int(k[1]))
    elif k[0]=="all":
        S= set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif k[0]=="empty":
        S= set()