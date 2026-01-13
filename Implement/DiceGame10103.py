n= int(input())
c, s= 100, 100
for i in range(n):
    c1, s1= map(int,input().split())
    if c1>s1:
        s -= c1
    elif c1<s1:
        c -= s1
print(c)
print(s)
