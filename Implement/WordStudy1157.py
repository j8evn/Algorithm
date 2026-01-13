ss= input().strip()
a= [0]*26
ss= ss.upper()
for i in range(len(ss)):
    a[ord(ss[i])-ord('A')] += 1
mm= max(a)
cnt, idx= 0, 0
for i in range(26):
    if (mm==a[i]):
        cnt += 1
        idx= i
if (cnt==1):
    print(chr(ord('A')+idx))
else:
    print("?")
