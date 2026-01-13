S= input().strip()
A= []
for i in range(len(S)):
    A.append(S[i:])
A.sort()
print('\n'.join(A))