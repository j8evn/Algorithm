N= int(input())
A= [0]*26
for _ in range(N):
    s= input().strip()
    A[ord(s[0])-ord('a')] += 1

ans= ""
for i in range(26):
    if A[i]>=5:
        ans += chr(ord('a')+i)

if ans:
    print(ans)
else:
    print("PREDAJA")