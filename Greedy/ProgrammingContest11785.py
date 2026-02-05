import sys
input= sys.stdin.readline

T= int(input())
for _ in range(T):
    N, L= map(int,input().split())
    A= list(map(int,input().split()))
    A.sort()
    s, cnt, total= 0, 0, 0
    for i in range(N):
        if s + A[i] > L:
            break
        s += A[i]
        cnt += 1
        total += s
    print("Case {}:".format(_+1), cnt, s, total)