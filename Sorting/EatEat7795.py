import sys
input= sys.stdin.readline

T= int(input())
for _ in range(T):
    N, M= map(int,input().split())
    A= list(map(int,input().split()))
    B= list(map(int,input().split()))
    A.sort()
    B.sort()
    cnt= 0
    a, b= 0, 0
    while a<N and b<M:
        if A[a]<=B[b]:
            a += 1
        else:
            if b+1<M and B[b+1]<A[a]:
                b += 1
            else:
                cnt += b+1
                a += 1
    print(cnt)