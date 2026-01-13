K= int(input())
s= input().strip()
ans= ""
for i in range(len(s)):
    if (ord(s[i])-3*(i+1)-K) < ord('A'):
        ans += chr(ord('Z')-ord('A')%(ord(s[i])-3*(i+1)-K)+1)
    else:
        ans += chr((ord(s[i])-3*(i+1)-K))
print(ans)