import sys
input= sys.stdin.readline

N, M= map(int,input().split())
if N==0:
    print(0)
else:
    A= list(map(int,input().split()))
    cnt= 0
    ss= 0
    for i in range(N):
        if ss+A[i] > M:
            ss= 0
            cnt += 1
        ss += A[i]
    if ss > 0:
        cnt += 1
    print(cnt)