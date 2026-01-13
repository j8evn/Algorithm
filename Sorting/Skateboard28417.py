N= int(input())
R= []
for _ in range(N):
    A= list(map(int,input().split()))
    r= max(A.pop(0),A.pop(0))
    A.sort()
    t= A[-1]+A[-2]
    R.append(r+t)
print(max(R))