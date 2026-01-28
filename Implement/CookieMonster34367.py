C= list(input().strip())
C= map(int,C)
C= sum(C)
while C>9:
    C= list(map(int,str(C)))
    C= sum(C)
print(C)