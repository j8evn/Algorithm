n= int(input())
N= []
for _ in range(n):
    N.append(list(map(int,input().split())))
N.sort(key=lambda x:x[0])
N.sort(key=lambda x:x[1])
for i in range(n):
    N[i]= map(str,N[i])
    print(' '.join(N[i]))
