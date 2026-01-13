import sys
input= sys.stdin.readline

def reverse(s):
    k= ""
    for i in range(len(s)-1,-1,-1):
        k += s[i]
    return k

ll= list(map(int,input().split()))
while (len(ll)<=ll[0]):
    t= list(map(int,input().split()))
    for i in range(len(t)):
        ll.append(t[i])
n= ll.pop(0)

R= []
for i in range(n):
    R.append(int(reverse(str(ll[i]))))
R.sort()
R= map(str,R)
print('\n'.join(R))