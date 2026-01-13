V= [False]*100000
for k in range(1,10000):
    if V[k]==True:
        continue
    i= k
    while i<10000:
        a= str(i)
        b= i
        for j in range(len(a)):
            b += int(a[j])
        V[b]= True
        i= b
for i in range(1,10001):
    if V[i]==False:
        print(i)