N= int(input())
n = 0
num = 0
while True:
    n += 1
    t = str(n)
    if '666' in t:
        num += 1
        if num==N:
            break
print(t)