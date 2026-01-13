def mulmat(a,b):
    n, c= len(a), []
    for i in range(n):
        c.append([0] *n)
    for i in range(n):
        for j in range(n):
            ss= 0
            for k in range(n):
                ss += a[i][k]*b[k][j]
                ss= ss % B
            c[i][j]= ss
    return c

def mpow(a,b):
    s = [[1,0],[0,1]]
    while (b>0):
        if (b%2==1):
            s= mulmat(s, a)
        a= mulmat(a, a)
        b= b //2
    return s

B= 1000000
N= int(input())
if (N==0):
	print(0)
else:
	A= [[1,1],[1,0]]
	A= mpow(A, N-1)
	print(A[0][0])
