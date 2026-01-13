T= int(input())
for i in range(T):
    n, k= map(int,input().split())
    N= list(map(int,input().split()))
    cnt= 0
    for j in range(n):
        cnt += N[j]//k
    print(cnt)
