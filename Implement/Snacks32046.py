while True:
    n= int(input())
    if n==0:
        break
    a= list(map(int,input().split()))
    m= 0
    for k in range(n):
        if (m+a[k] <= 300):
            m += a[k]
    print(m)
