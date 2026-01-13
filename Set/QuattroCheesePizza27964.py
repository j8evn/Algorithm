N= int(input())
A= list(input().split())
cheese= set()
for i in range(N):
    if "Cheese" in A[i] and A[i] not in cheese:
        if A[i][len(A[i])-6:]=="Cheese":
            cheese.add(A[i])
if len(cheese)>=4:
    print("yummy")
else:
    print("sad")