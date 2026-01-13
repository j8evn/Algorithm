S= input().strip()
A= [0]*26
for i in range(len(S)):
    A[ord(S[i])-ord('a')] += 1
A= map(str,A)
print(' '.join(A))