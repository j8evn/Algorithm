n, k= map(int,input().split())
a= 1
for i in range(1,n+1):
    a= a*i
b= 1
for i in range(1,k+1):
    b= b*i
c= 1
for i in range(1,n-k+1):
    c= c*i
print(a//(b*c))