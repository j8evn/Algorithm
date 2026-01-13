import sys
input= sys.stdin.readline

T= int(input())
for _ in range(T):
    ss= input().rstrip()
    R= []
    re= ""
    for i in range(len(ss)):
        if ss[i]==" ":
            k= ""
            for j in range(len(re)-1,-1,-1):
                k += re[j]
            R.append(k)
            re= ""
        else:
            re += ss[i]
    k= ""
    for j in range(len(re)-1,-1,-1):
        k += re[j]
    R.append(k)
    print(' '.join(R))