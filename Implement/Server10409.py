n, t= map(int,input().split())
ll= list(map(int,input().split()))
ss, cnt= 0, 0
for i in range(n):
    ss= ss+ ll[i]
    if(ss>t):
        break
    else:
        cnt= cnt+ 1
print(cnt)
