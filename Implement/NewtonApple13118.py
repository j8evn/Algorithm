p= list(map(int,input().split()))
x, y, r= map(int,input().split())
R= 0
for i in range(4):
    if x==p[i]:
        R= i+1
print(R)