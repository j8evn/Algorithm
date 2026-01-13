s= input().strip()
a= ["a","e","i","o","u"]
cnt= 0
for i in range(len(s)):
    if s[i] in a:
        cnt += 1
print(cnt)