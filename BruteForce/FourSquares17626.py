def Check(N, P):
    for i in range(len(P)):
        if(P[i]==N):
            return 1
    for i in range(len(P)):
        for j in range(len(P)):
            if(P[i]+P[j]==N):
                return 2
    for i in range(len(P)):
        for j in range(len(P)):
            for k in range(len(P)):
                if(P[i]+P[j]+P[k]==N):
                    return 3
    return 4

N= int(input())
P=[]
n= 1
while(n*n<=50000):
    P.append(n*n)
    n+= 1
print(Check(N,P))
