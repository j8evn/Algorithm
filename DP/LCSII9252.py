import sys
sys.setrecursionlimit(5000)

def lcs(i, j):
    global ss
    if ((i==L1) or (j==L2)):
        SR.append(ss)
        ss= ""
        return 0
    if (dp[i][j] !=-1):
        return dp[i][j]
    if (S1[i] == S2[j]):
        ss += S1[i]
        return lcs(i+1, j+1)+1
    t1 = lcs(i, j+1)
    t2 = lcs(i+1, j)
    dp[i][j] = max(t1, t2)
    return dp[i][j]

S1= input()
S2= input()
L1, L2 = len(S1), len(S2)
ss, SR= "", []
dp= []
for i in range(L1+1):
    dp.append([-1]*(L2+1))

mm= lcs(0,0)
for i in range(len(SR)):
    if len(SR[i])==mm:
        print(mm)
        print(SR[i])
        break
print(ss)
print(dp)