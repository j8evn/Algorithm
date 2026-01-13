A= []
A.append(int(input()))
for i in range(9):
    A.append(A[i]+int(input()))

mm, mx= 100, 0
for i in range(10):
    if mm>=abs(A[i]-100):
        mm= abs(A[i]-100)
        mx= A[i]
print(mx)