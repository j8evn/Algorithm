T= int(input())
for _ in range(T):
    n, m= map(int,input().split())
    cnt= 0
    for b in range(1,n):
        for a in range(1,b):
            tt= ((a*a)+(b*b)+m)/(a*b)
            if tt==int(tt):
                cnt += 1
    print(cnt)