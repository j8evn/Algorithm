n= int(input())
N= [0]*n
for i in range(n):
    k= int(input())
    N[k-1]= i+1
N= map(str,N)
print("\n".join(N))