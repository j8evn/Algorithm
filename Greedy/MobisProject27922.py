import sys
input= sys.stdin.readline

N, K= map(int,input().split())
s1, s2, s3= [], [], []
for _ in range(N):
    a, b, c= map(int,input().split())
    s1.append(a+b)
    s2.append(b+c)
    s3.append(a+c)
    
s1.sort()
s2.sort()
s3.sort()
print(max(sum(s1[N-K:N]),sum(s2[N-K:N]),sum(s3[N-K:N])))