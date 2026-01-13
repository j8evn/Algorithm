def pal():
    l,r=0,len(S)-1
    while (l<r): 
            if (S[l]!=S[r]):
                print(0)
                return
            l,r=l+1,r-1
    print(1)
    return

S=input()
n=len(S)
pal()
