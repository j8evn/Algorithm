def Palin(s):
    l, r= 0, len(s)-1
    while(l<r):
        if s[l]!=s[r]:
            return "no"
        l, r= l+1, r-1
    return "yes"

while True:
    s= input().strip()
    if s=='0':
        break
    print(Palin(s))
