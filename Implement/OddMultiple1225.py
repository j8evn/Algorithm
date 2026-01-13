A, B= input().split()
A= list(map(int,A))
B= list(map(int,B))
cal= 0
for i in range(len(A)):
    for j in range(len(B)):
        cal += A[i]*B[j]
print(cal)