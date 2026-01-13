def reverse(s):
    k= ""
    for i in range(len(s)-1,-1,-1):
        k += s[i]
    return k

ss= input().strip()
ll= []

for i in range(1,len(ss)-1):
    for j in range(i+1,len(ss)):
        ll.append(reverse(ss[0:i])+reverse(ss[i:j])+reverse(ss[j:]))
ll.sort()
print(ll[0])