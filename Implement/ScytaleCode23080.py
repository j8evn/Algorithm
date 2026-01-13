k= int(input())
s= input().strip()
r= ""
for i in range(len(s)):
    if i%k==0:
        r += s[i]
print(r)