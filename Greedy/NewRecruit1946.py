import sys
input= sys.stdin.readline

T= int(input())
for _ in range(T):
    N= int(input())
    A= []
    for _ in range(N):
        A.append(list(map(int,input().split())))
    A.sort(key=lambda x:x[1])
    A.sort(key=lambda x:x[0])
    cnt= 0
    mm= 100001
    for i in range(1,N):
        mm= min(mm, A[i-1][1])
        if A[i][1]>mm:
            cnt += 1
    print(N-cnt)