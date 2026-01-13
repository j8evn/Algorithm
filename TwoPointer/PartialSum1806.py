N, S= map(int,input().split())
A= list(map(int,input().split()))
l, r= 0, 0
sum= 0
mm= 1000000000

while True:
    if sum>=S:
        mm= min(mm,r-l)
        sum -= A[l]
        l += 1
    elif r==N:
        break
    else:
        sum += A[r]
        r += 1

if mm==1000000000:
    print(0)
else:
    print(mm)