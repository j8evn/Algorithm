import sys
input= sys.stdin.readline

def Palin1(ss, l, r):
    while l<r:
        if ss[l] != ss[r]:
            return False
        l, r= l+1, r-1
    return True

def Palin2(ss):
    l, r= 0, len(ss)-1
    while l<r:
        if ss[l] == ss[r]:
            l, r= l+1, r-1
        else:
            if l+1<=r and Palin1(ss,l+1,r)==True:
                return 1
            elif l<=r-1 and Palin1(ss,l,r-1)==True:
                return 1
            else:
                return 2
    return 0

R= []
T= int(input())
for _ in range(T):
    s= input().strip()
    R.append(Palin2(s))

R= map(str,R)
print("\n".join(R))