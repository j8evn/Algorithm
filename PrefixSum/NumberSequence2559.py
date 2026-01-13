n, k= map(int,input().split())
a= list(map(int,input().split()))
ss= sum(a[0:k])
mm= ss
for i in range(n-k):
    ss= ss -a[i] +a[i+k]
    mm= max(mm, ss)
print(mm)
