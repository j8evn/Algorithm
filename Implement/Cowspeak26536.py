n= int(input())
for _ in range(n):
    A= list(input().split())
    s= ""
    for i in range(len(A)):
        m= A[i].count('M')
        o= A[i].count('O')
        ascii= m*16+ o
        s += chr(ascii)
    print(s)