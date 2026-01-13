n= int(input())
total= (n*(n-1))//2
halfway= total//2

s, e = 1, n
while s<=e:
    mid= (s+e)//2
    if (mid*(mid-1))//2 == halfway:
        ans= mid
        break
    elif (mid*(mid-1))//2 < halfway:
        ans= mid # 정확히 맞지 않는 경우 근접한 값 저장장
        s= mid+1
    else:
        e= mid-1
print(n-ans)