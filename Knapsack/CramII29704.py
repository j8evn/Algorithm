def knapsack(n, W):
    dp= [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                dp[i][w]= 0
            elif D[i-1] <= w:
                dp[i][w]= max(M[i-1]+dp[i-1][w-D[i-1]], dp[i-1][w])
            else:
                dp[i][w]= dp[i-1][w]
    return dp[n][W]

D, M= [], []
N, T = map(int,input().split())
for _ in range(N):
    d, m = map(int,input().split())
    D.append(d)
    M.append(m)
c= knapsack(N,T)
print(sum(M)-c)