n= int(input())
for i in range(n):
    t= int(input())
    p=[1,1,1]
    for j in range(100):
        p.append(p[j]+p[j+1])
    print(p[t-1])
