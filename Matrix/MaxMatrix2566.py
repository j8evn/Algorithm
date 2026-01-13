A=[]
mm,r,c=-1,-1,-1
for i in range(9):
    A.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        if (A[i][j]>mm):
            mm,r,c=A[i][j],i,j
print(mm)
print(r+1,c+1)
            
