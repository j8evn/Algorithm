import sys
input= sys.stdin.readline

T= int(input())
for _ in range(T):
    N= int(input())
    A= list(map(int,input().split()))
    for i in range(1,N):
        A[i] += A[i-1]
    mm= -10000000
    for i in range(N):
        mm= max(mm,A[i])
        for j in range(i):
            mm= max(mm,A[i]-A[j])
    print(mm)