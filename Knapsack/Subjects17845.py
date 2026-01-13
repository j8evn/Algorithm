def knapsack(n, W):
    dp= [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                dp[i][w]= 0
            elif T[i-1] <= w:
                dp[i][w]= max(I[i-1]+dp[i-1][w-T[i-1]], dp[i-1][w])
            else:
                dp[i][w]= dp[i-1][w]
    return dp[n][W]

I, T= [], []
N, K = map(int,input().split())
for _ in range(K):
    i, t = map(int,input().split())
    I.append(i)
    T.append(t)
print(knapsack(K,N))