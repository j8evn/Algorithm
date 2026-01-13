N= int(input())
A= []
for i in range(N):
    A.append(i+1)
    if (i+1)%6==0:
        A.append("Go!")
if A[-1]=="Go!":
    print(*A)
else:
    A.append("Go!")
    print(*A)
