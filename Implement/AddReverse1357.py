def reverse(s):
    k= ""
    for i in range(len(s)-1,-1,-1):
        k += s[i]
    return k

X, Y= input().split()
ans= reverse(str(int(reverse(X))+int(reverse(Y))))
print(int(ans))