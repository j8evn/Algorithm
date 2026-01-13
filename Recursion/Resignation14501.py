def Proc(loc):
    if loc>=N:
        return 0
    tt= Proc(loc+1)
    if loc+A[loc][0] <= N:
        tt= max(tt,Proc(loc+A[loc][0])+A[loc][1])
    return tt

N= int(input())
A= []
for _ in range(N):
    A.append(list(map(int,input().split())))
print(Proc(0))

'''
def Proc(loc):
    if loc>=N:
        return 0
    if dp[loc]!=-1:
        return dp[loc]
    dp[loc]= Proc(loc+1)
    if loc+A[loc][0] <= N:
        dp[loc]= max(dp[loc],Proc(loc+A[loc][0])+A[loc][1])
    return dp[loc]

N= int(input())
A= []
dp= [-1]*(N+1)
for _ in range(N):
    A.append(list(map(int,input().split())))
print(Proc(0))
'''