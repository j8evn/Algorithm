import sys
input= sys.stdin.readline

while True:
    N, M= map(int,input().split())
    if N==M==0:
        break
    S= set()
    for _ in range(N):
        S.add(int(input()))
    cnt= 0
    for _ in range(M):
        s= int(input())
        if s in S:
            cnt += 1
    print(cnt)