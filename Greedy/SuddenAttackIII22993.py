N= int(input())
A= list(map(int,input().split()))
a= A[0]
A= sorted(A[1:])

i= 0
while i<N-1:
    if a>A[i]:
        a += A[i]
        i += 1
    else:
        break

if i!=N-1:
    print("No")
else:
    print("Yes")