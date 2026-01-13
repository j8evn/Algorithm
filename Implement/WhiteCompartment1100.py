Chess= []
for _ in range(8):
    Chess.append(list(input().strip()))
w= 0
for i in range(0,8,2):
    for j in range(0,8,2):
        if Chess[i][j]=="F":
            w += 1
for i in range(1,8,2):
    for j in range(1,8,2):
        if Chess[i][j]=="F":
            w += 1
print(w)