import sys
input= sys.stdin.readline

def IsPalin(a):
    l, r= 0, len(a)-1
    while (l<r):
        if a[l]!=a[r]:
            return False
        l, r= l+1, r-1
    return True

N= int(input())
S= set()
for _ in range(N):
    ll= list(input().strip())
    ll.reverse()
    if IsPalin(''.join(ll)):
        ans= ll
    if ''.join(ll) in S:
        ans= ll
    else:
        ll.reverse()
        S.add(''.join(ll))
print(len(ans),ans[len(ans)//2])