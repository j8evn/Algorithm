s= input()
A=[]
d= ord('a')-ord('A')
for i in range(len(s)):
    if 'A'<=s[i] and s[i]<='Z':
        A.append(chr(ord(s[i])+d))
    elif 'a'<=s[i] and s[i]<='z':
        A.append(chr(ord(s[i])-d))
print(''.join(A))
