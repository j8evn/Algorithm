n, k= input().split()
n= int(n)
S= set()
for _ in range(n):
    S.add(input().strip())

if k=="Y":
    print(len(S))
elif k=="F":
    print(len(S)//2)
elif k=="O":
    print(len(S)//3)