def knapsack(n, W):
    dp= [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                dp[i][w]= 0
            elif wt[i-1] <= w:
                dp[i][w]= max(val[i-1]+dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w]= dp[i-1][w]
    return dp[n][W]

T= int(input())
for _ in range(T):
    wt, val= [], []
    N, K = map(int,input().split())
    for _ in range(N):
        v, w = map(int,input().split())
        wt.append(w)
        val.append(v)
    print(knapsack(N,K))