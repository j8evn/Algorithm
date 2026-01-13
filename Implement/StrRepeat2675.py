T=int(input())
for j in range(T):
    n,s=input().strip().split()
    n=int(n)
    for i in range(len(s)):
        print(s[i]*n, end='')
    print()
