N=int(input())
for i in range(N):
        print(" "*(N-i-1)+"*"*(2*i+1))
N=N-1
for i in range(N):
        print(" "*(i+1)+"*"*(2*N-(2*i+1)))
