def Palin(N):
    l, r= 0, len(N)-1
    while (l<r):
        if N[l] != N[r]:
            return "NO"
        l, r= l+1, r-1
    return "YES"

T= int(input())
for i in range(T):
    n= input()
    rn= ''
    for j in range(len(n)):
        rn += n[len(n)-j-1]
    ss= int(n)+int(rn)
    print(Palin(str(ss)))
