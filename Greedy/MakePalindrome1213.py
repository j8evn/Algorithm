s= input().strip()
A= [0]*26
for i in range(len(s)):
    A[ord(s[i])-ord('A')] += 1

t, k= 0, None
for i in range(26):
    if A[i]%2==1:
        t += 1
        k= chr(i+ord('A'))

if t==0:
    ans= []
    for i in range(26):
        for _ in range(A[i]//2):
            ans.append(chr(i+ord('A')))
    tt= list(reversed(ans))
    ans += tt
    print(''.join(ans))
elif t==1:
    ans= []
    for i in range(26):
        for _ in range(A[i]//2):
            ans.append(chr(i+ord('A')))
    tt= list(reversed(ans))
    ans.append(k)
    ans += tt
    print(''.join(ans))
else:
    print("I'm Sorry Hansoo")