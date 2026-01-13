def Check():
    loc= [-1]*26
    cnt= [0]*26
    for i in range(len(S)):
        tt= ord(S[i])-ord('a')
        cnt[tt] += 1
        if cnt[tt]>2:
            return "NO"
        if loc[tt]!=-1:
            if (i-loc[tt])%2==0:
                return "NO"
        loc[tt]= i
    return "YES"

S= input().strip()
print(Check())