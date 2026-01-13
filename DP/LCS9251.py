import sys
sys.setrecursionlimit(5000)

def lcs(i,j):
    if ((i==L1) or (j==L2)):
        return 0
    if (dp[i][ j] !=-1):
        return dp[i][j]
    if (S1[i] == S2[ j]):
        return lcs(i+1, j+1)+1
    t1 = lcs(i, j+1)
    t2 = lcs(i+1, j)
    dp[i][j] = max(t1, t2)
    return dp[i][j]

S1= input()
S2= input()
L1, L2 = len(S1), len(S2)
dp = []
for i in range(L1+1):
    dp.append([-1]*(L2+1))
print(lcs(0,0))