N, K, P= map(int,input().split())
A= list(map(int,input().split()))

cnt= 0
for i in range(0,len(A),K):
    if A[i:i+K].count(0)<P:
        cnt += 1
print(cnt)