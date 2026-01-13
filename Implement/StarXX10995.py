n= int(input())
s= ''
for _ in range(n):
    s += "* "
for i in range(1,n+1):
    if i%2==0:
        print(" "+s)
    else:
        print(s)