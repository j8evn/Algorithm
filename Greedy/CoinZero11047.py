# 동전이 다음 큰 동전을 나눌 수 있을 때만 그리디 가능

N, T = map(int,input().split())
A = []
for _ in range(N):
    A.append(int(input()))

ss= 0
for i in range(N-1,-1,-1):
    ss = ss+ T // A[i]
    T= T % A[i]
print (ss)