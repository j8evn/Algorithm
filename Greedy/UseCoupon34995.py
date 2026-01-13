n, s= input().split()
n= int(n)
p= input().strip()

if len(s)<len(p):
    print(-1)
elif len(s)>len(p):
    ans= ""
    for i in range(n):
        if s[i]=='?':
            ans += '1'
        else:
            ans += s[i]
    print(ans)
else:
    ans= ""
    for i in range(n):
        if s[i]=='?':
            if p[i]=='9':
                ans += '9'
            else:
                ans += str(int(p[i])+1)
        else:
            ans += s[i]
    if ans>=p:
        print(ans)
    else:
        print(-1)