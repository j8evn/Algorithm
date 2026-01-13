A= []
for _ in range(8):
    A.append(list(input().split()))
A.sort(key=lambda x:x[0])

s= [10, 8, 6, 5, 4, 3, 2, 1]
B, R= 0, 0
for i in range(8):
    if A[i][1]=="B":
        B += s[i]
    else:
        R += s[i]
if B>R:
    print("Blue")
else:
    print("Red")