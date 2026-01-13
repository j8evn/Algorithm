n= int(input())
cnt= 0
for i in range(100):
    for j in range(100):
        if n-i-j==0:
            cnt += 1
print(cnt)