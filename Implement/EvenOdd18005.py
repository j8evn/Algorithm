n= int(input())
n1= n*(n+1)//2
n2= (n+1)*(n+2)//2-1
if n1%2!=n2%2:
    print(0)
else:
    if n1%2==0:
        print(2)
    else:
        print(1)