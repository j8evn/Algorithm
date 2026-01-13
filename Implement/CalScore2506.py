n= int(input())
G= list(map(int,input().split()))
t, p= 0, 0
for i in range(n):
    if G[i]==1:
        p += 1
        t= t+p
    else:
        p= 0
print(t)
