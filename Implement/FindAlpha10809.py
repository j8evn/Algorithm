F=[-1]*26
S=input().strip()
for i in range(len(S)):
#    print(ord(S[i])-ord('a'))
    t=ord(S[i])-ord('a')
    if (F[t]==-1):
        F[t]=i
F=list(map(str,F))
print(' '.join(F))
