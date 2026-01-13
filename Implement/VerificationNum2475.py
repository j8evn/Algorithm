n= list(map(int,input().split()))
n.append(0)
for i in range(5):
    n[5] += (n[i]**2)
print(n[5]%10)
