def pal(n):
    ss= n
    while(n>0):
        ss= ss*10+n%10
        n= n//10
    return ss

def pal2(n):
    ss= n
    n= n//10
    while(n>0):
        ss= ss*10+n%10
        n= n//10
    return ss

n= int(input())
cnt= 0
for i in range(1,10**5):
    if(pal(i)>n):
        break
    cnt= cnt+ 1
for i in range(1,10**5):
    if(pal2(i)>n):
        break
    cnt= cnt+ 1
print(cnt)
