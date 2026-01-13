a= int(input())
b= int(input())
s= 0
for i in range(a,b+1):
    cnt= 0
    for j in range(1,i+1):
        if i%j==0:
            cnt += 1
    if cnt==4:
        s += 1
print("The number of RSA numbers between {:d} and {:d} is {:d}".format(a,b,s))