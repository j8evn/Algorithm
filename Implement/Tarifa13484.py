X= int(input())
N= int(input())
R= X*N
for i in range(N):
    R -= int(input())
print(R+X)