n, a, b= map(int,input().split())
R= [0]*3
for i in range(1,n+1):
    if i%a==0 and i%b==0:
        R[2] += 1
    elif i%a==0:
        R[0] += 1
    elif i%b==0:
        R[1] += 1
print(*R)