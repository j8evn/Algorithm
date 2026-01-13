s= input().strip()
dic= {}
for i in range(len(s)):
    if s[i] in dic:
        dic[s[i]] += 1
    else:
        dic[s[i]]= 1

v= []
for d in dic:
    if dic[d]%2==0:
        v.append(True)
    else:
        v.append(False)

if False in v and True in v:
    print(2)
elif False in v:
    print(1)
elif True in v:
    print(0)