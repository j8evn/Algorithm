S= input().strip()
A= set()
for i in range(len(S)):
    for j in range(i,len(S)):
        A.add(S[i:j+1])
print(len(A))