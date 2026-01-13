N, K= map(int,input().split())
A= list(map(int,input().split()))
cnt= 0
for i in range(N-1, -1, -1):
    if cnt==K:
        break
    mm, mi = A[i], i
    for j in range(i-1, -1, -1):
        if (mm < A[j]):
            mm, mi = A[j], j
    if mi != i:
        cnt += 1
        A[mi], A[i] = A[i], A[mi]
if cnt==K:
    print(A[mi], A[i+1])
else:
    print(-1)