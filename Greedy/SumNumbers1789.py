n= int(input())
i, cnt= 0, 0
while n>i:
    i += 1
    n -= i
    cnt += 1
print(cnt)