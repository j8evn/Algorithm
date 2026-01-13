A, B= map(int,input().split())
cnt= 1
while A!=B:
    cnt += 1
    cur= B
    if B%10==1:
        B= B//10
    elif B%2==0:
        B= B//2
    if cur==B:
        print(-1)
        break
else:
    print(cnt)