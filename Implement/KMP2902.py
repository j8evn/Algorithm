ss= input().strip()
ans= ""
for i in range(len(ss)):
    if ord('A') <= ord(ss[i]) <= ord('Z'):
        ans += ss[i]
print(ans)
