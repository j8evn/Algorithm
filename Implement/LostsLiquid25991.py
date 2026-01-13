n= int(input())
c= list(map(float,input().split()))

cal= 0
for i in range(n):
    cal += c[i]*c[i]*c[i]
print(cal**(1/3))