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

wt, val= [], []
N, K = map(int,input().split())
for _ in range(N):
    w, v = map(int,input().split())
    wt.append(w)
    val.append(v)
print(knapsack(N,K))


'''
def knap(n, left):
    if (n==N):
        return 0
    if (dp[n][left] != -1):
        return dp[n][left]
    tt = knap(n+1, left)
    if (left >= A[n][0]):
        tt = max(tt, knap(n+1, left-A[n][0])+A[n][1])
    dp[n][left] = tt
    return tt

N, K = map(int,input().split())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))
dp = []
for i in range(N+1):
    dp.append([-1]* (K+1))
print(knap(0, K))
'''