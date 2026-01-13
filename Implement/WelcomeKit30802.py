N= int(input())
S= list(map(int,input().split()))
T, P= map(int,input().split())
cnt= 0
for i in range(6):
    if S[i]%T==0:
        cnt += S[i]//T
    else:
        cnt += S[i]//T+1
print(cnt)
print(N//P, N%P)