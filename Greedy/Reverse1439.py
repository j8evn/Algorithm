S= input().strip()
cnt0, cnt1= 0, 0
if S[0]=="0":
    cnt0 += 1
else:
    cnt1 += 1

for i in range(1,len(S)):
    if S[i-1]==S[i]:
        continue
    else:
        if S[i]=="0":
            cnt0 += 1
        else:
            cnt1 += 1

print(min(cnt0,cnt1))