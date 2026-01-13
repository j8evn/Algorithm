import sys
input= sys.stdin.readline

L, N= map(int,input().split())
dic= {}
a= "aeiou"
b= "osx"
for i in range(L):
    s, p= input().split()
    dic[s]= p
R= []
for i in range(N):
    t= input().strip()
    if t in dic:
        R.append(dic[t])
    elif (t[-2] not in a) and (t[-1]=='y'):
        R.append(t[:-1]+'ies')
    elif (t[-1] in b):
        R.append(t+'es')
    elif (t[-1]=='h'):
        if (t[-2]=='c'):
            R.append(t+'es')
        elif (t[-2]=='s'):
            R.append(t+'es')
    else:
        R.append(t+'s')
print('\n'.join(R))