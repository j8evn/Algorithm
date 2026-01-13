import sys
input= sys.stdin.readline

def reverse(s):
    k= ""
    for i in range(len(s)-1,-1,-1):
        k += s[i]
    return k

S= input().rstrip()
R= ""
re= ""
i= 0
while (i<len(S)):
    if S[i]==" ":
        R += reverse(re)
        R += " "
        re= ""
        i += 1
    elif S[i]=="<":
        R += reverse(re)
        re= ""
        a= "<"
        while S[i]!=">":
            i += 1
            a += S[i]
        R += a
        i += 1
    else:
        re += S[i]
        i += 1
R += reverse(re)
print(R)