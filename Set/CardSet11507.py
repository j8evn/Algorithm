S= input().strip()
A= [13, 13, 13, 13]
s= set()
for i in range(0,len(S),3):
    if S[i]=='P':
        if S[i:i+3] in s:
            A[0]= False
            break
        else:
            A[0] -= 1
            s.add(S[i:i+3])
    elif S[i]=='K':
        if S[i:i+3] in s:
            A[1]= False
            break
        else:
            A[1] -= 1
            s.add(S[i:i+3])
    elif S[i]=='H':
        if S[i:i+3] in s:
            A[2]= False
            break
        else:
            A[2] -= 1
            s.add(S[i:i+3])
    else:
        if S[i:i+3] in s:
            A[3]= False
            break
        else:
            A[3] -= 1
            s.add(S[i:i+3])
if False in A:
    print("GRESKA")
else:
    print(*A)