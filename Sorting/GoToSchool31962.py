A= [-1]
n, x= map(int,input().split())
for _ in range(n):
    s, t= map(int,input().split())
    if s+t <= x:
        A.append(s)
A.sort()
print(max(A))
