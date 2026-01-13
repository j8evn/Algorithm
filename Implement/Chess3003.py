c= [1,1,2,2,2,8]
ss= list(map(int,input().split()))
for i in range(6):
    c[i]= c[i]- ss[i]
c= map(str,c)
print(" ".join(c))
