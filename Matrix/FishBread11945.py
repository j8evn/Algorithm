N, M= map(int, input().split())
for i in range(N):
    A =list(input())
    l, r= 0, M-1
    while (l<r):
        A[l], A[r]= A[r], A[l]
        l = l+1
        r = r-1
    print(''.join(A))
