def knapsack(n, W):
    dp= [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                dp[i][w]= 0
            elif K[i-1] <= w:
                dp[i][w]= max(S[i-1]+dp[i-1][w-K[i-1]], dp[i-1][w])
            else:
                dp[i][w]= dp[i-1][w]
    return dp[n][W]

K, S= [], []
N, T = map(int,input().split())
for _ in range(N):
    k, s = map(int,input().split())
    K.append(k)
    S.append(s)
print(knapsack(N,T))