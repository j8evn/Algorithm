while True:
    n= int(input())
    if n==-1:
        break
    A= []
    for i in range(1,n-1):
        if n%i==0:
            A.append(i)
    if sum(A)==n:
        A= map(str,A)
        print(n, "=", " + ".join(A))
    else:
        print(n, "is NOT perfect.")
