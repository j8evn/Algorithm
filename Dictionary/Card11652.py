N= int(input())
D= {}
for i in range(N):
    n= int(input())
    if n in D:
        D[n] += 1
    else:
        D[n]= 1
mm= -1
for d in D:
    mm= max(mm,D[d])
R= []
for d in D:
    if D[d]==mm:
        R.append(d)
print(min(R))