s= input().strip()
h= 10
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        h= h+ 5
    else:
        h= h+ 10
print(h)