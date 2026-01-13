n= int(input())
for i in range(1,1000001):
    if i==n:
        print(0)
        break
    k= str(i)
    k= list(map(int,k))
    if i+sum(k)==n:
        print(i)
        break