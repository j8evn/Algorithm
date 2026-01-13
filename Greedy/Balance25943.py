W= [100,50,20,10,5,2,1]
n= int(input())
N= list(map(int,input().split()))
l, r= 0, 0
for i in range(n):
    if (r>=l):
        l += N[i]
    else:
        r += N[i]
t= abs(l-r)
cnt= 0
for i in range(len(W)):
    cnt += t//W[i]
    t= t%W[i]
print(cnt)
