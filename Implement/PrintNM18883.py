N, M= map(int,input().split())
t= []
for i in range(1,N*M+1):
    t.append(i)
    if i%M==0:
        print(*t)
        t= []