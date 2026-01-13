T={1:1,2:2,3:-1}
A=[]

for i in range(10):
    t=int(input())
    A.append(T[t])

if (sum(A)%4==0):
    print("N")
elif (sum(A)%4==1)or(sum(A)%4==-3):
    print("E")
elif (sum(A)%4==2)or(sum(A)%4==-2):
    print("S")
else:
    print("W")