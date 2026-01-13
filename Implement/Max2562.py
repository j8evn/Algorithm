A=[]
for i in range(9):
    A.append (int(input()))
mm=-1000001
mi=0
for i in range(9):
    if (mm<A[i]):
        mm=A[i]
        mi=i+1
print(mm)
print(mi)
