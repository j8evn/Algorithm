S1= input()
S2= input()
S3= input()
L1, L2, L3 = len(S1)+1, len(S2)+1, len(S3)+1
dp= []
for _ in range(L1):
    t= []
    for _ in range(L2):
        t.append([0]*L3)
    dp.append(t)

for i in range(1, L1):
    for j in range(1, L2):
        for k in range(1,L3):
            if (S1[i-1] == S2[j-1] == S3[k-1]):
                dp[i][j][k] = dp[i-1][j-1][k-1]+1
            else:
                dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1],
                                  dp[i-1][j-1][k],dp[i][j-1][k-1],dp[i-1][j][k-1])
print(dp[-1][-1][-1])