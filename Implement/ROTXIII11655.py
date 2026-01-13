S= input()
N= ""
for i in range(len(S)):
    if ord('a') <= ord(S[i]) <= ord('z'):
        N += chr((ord(S[i])-ord('a')+13)%26+ord('a'))
    elif ord('A') <= ord(S[i]) <= ord('Z'):
        N += chr((ord(S[i])-ord('A')+13)%26+ord('A'))
    else:
        N += S[i]
print(N)