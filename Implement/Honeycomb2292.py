n= int(input())
cnt= 1
a= 1
i= 1
while (a<n):
    for _ in range(6*i):
        a += 1
    i += 1
    cnt += 1
print(cnt)