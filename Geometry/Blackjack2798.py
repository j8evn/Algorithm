n, m= map(int,input().split())
N= list(map(int,input().split()))
mm= -1
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if N[i]+N[j]+N[k]<=m:
                mm= max(mm,N[i]+N[j]+N[k])
print(mm)