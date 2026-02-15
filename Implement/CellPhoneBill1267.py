N= int(input())
A= list(map(int, input().split()))
Y, M= 0, 0
for i in range(N):
    Y += (A[i]//30+1)*10
    M += (A[i]//60+1)*15
if Y<M:
    print('Y', Y)
elif Y>M:
    print('M', M)
else:
    print('Y M', Y)