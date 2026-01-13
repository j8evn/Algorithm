A= []
for _ in range(5):
    A.append(sum(list(map(int,input().split()))))
mm= max(A)
print(A.index(mm)+1, mm)