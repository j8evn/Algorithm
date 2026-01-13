P=int(input())
s=[0]*4
for i in range(P):
    G,C,N=map(int,input().split())
    if G==1:
        s[3]+=1
    elif (C==1)or(C==2):
        s[0]+=1
    elif C==3:
        s[1]+=1
    else:
        s[2]+=1
for i in range(4):
    print(s[i])
