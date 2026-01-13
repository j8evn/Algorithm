N= int(input())
a= input().strip()
first= False
cnt= 1
for i in range(N):
    if a[i]=='S':
        cnt += 1
    else:
        if first==False:
            first= True
        else:
            first= False
            cnt += 1
print(min(N,cnt))