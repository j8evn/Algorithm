A= list(map(int, input().split()))
B= list(map(int, input().split()))
a, b= 0, 0
L = None

for i in range(10):
    if (A[i]<B[i]):
        b += 3
        L= 'B'
    elif (A[i]>B[i]):
        a += 3
        L = 'A'
    else:
        a += 1
        b += 1

print(a,b)
if (a<b):
    print('B')
elif (a>b):
    print('A')
else:
    if (L==None):
        print('D')
    else:
        print(L)
