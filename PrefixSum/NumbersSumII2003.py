N, M= map(int,input().split())
A= list(map(int,input().split()))
for i in range(1,N):
    A[i] += A[i-1]
cnt= 0
for i in range(N):
    if A[i]==M:
        cnt += 1
    for j in range(i):
        if A[i]-A[j]==M:
            cnt += 1
print(cnt)