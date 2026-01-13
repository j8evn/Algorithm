a,b=input().strip().split()
a=list(a)
b=list(b)
a=list(map(int,a))
b=list(map(int,b))
a=a[2]*100+a[1]*10+a[0]
b=b[2]*100+b[1]*10+b[0]
if (a>b):
    print(a)
else:
    print(b)
