def gcd(a,b):
    if(a<b):
        a, b= b, a
    while(b>0):
        if(a%b==0):
            return b
        a, b= b, a%b

A= list(map(int, input().split()))
B= list(map(int, input().split()))
cnt= 0
for i in range(6):
    for j in range(6):
        if(A[i]>B[j]):
            cnt= cnt+ 1
g= gcd(cnt,36)
print(str(cnt//g)+"/"+str(36//g))
