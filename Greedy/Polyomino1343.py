s= input()
ans= ''
cnt= 0
for i in range(len(s)):
    if s[i]=='X':
        cnt += 1
    else:
        if cnt%2==1:
            break
        else:
            ans += 'AAAA'*(cnt//4)+'BB'*(cnt%4//2)
            cnt= 0
        ans += s[i]
if cnt%2==1:
    print(-1)
else:
    ans += 'AAAA'*(cnt//4)+'BB'*(cnt%4//2)
    print(ans)