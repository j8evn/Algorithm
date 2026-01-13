n= int(input())
if n==0:
    print(0)
else:
    f2, f1= 1, 0
    for i in range(n-1):
        t= f1
        f1= f2
        f2= f2+ t
    print(f2)
