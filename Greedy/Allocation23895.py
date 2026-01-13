import sys
input= sys.stdin.readline

T= int(input())
for t in range(T):
    N, B= map(int,input().split())
    A= list(map(int,input().split()))
    A.sort()
    cnt= 0
    ss= 0
    for i in range(N):
        ss += A[i]
        if ss>B:
            break
        cnt += 1
    print("Case #{:d}: {:d}".format(t+1,cnt))