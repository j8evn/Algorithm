import sys
input= sys.stdin.readline

P = [1]*1000001
P[0], P[1]= 0, 0
for i in range(2,1000001): 
    if (P[i] == 1):
        u = i*2
        while (u<1000001):
            P[u] = 0
            u =u+i

c= [0]*1000001
c[2]= 1
for i in range(3,1000001):
    if (P[i]==1) and (i%4==1):
        c[i]= 1

for i in range(1,1000001):
    P[i] += P[i-1]
    c[i] += c[i-1]

R= []
while True:
    L, U= map(int,input().split())
    if (L==-1) and (U==-1):
        break
    
    if (L>=1):
        x= P[U]-P[L-1]
        y= c[U]-c[L-1]
    elif (L<1) and (U>=0):
        x= P[U]
        y= c[U]
    elif (L<1) and (U<0):
        x= 0
        y= 0
        
    R.append(str(L)+" "+str(U)+" "+str(x)+" "+str(y))

print("\n".join(R))
