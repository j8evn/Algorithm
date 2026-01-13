N= int(input())
dic= {}
for _ in range(N):
    a, b= input().split()
    if a in dic:
        dic[a] += int(b)
    else:
        dic[a]= int(b)

check= False
for d in dic:
    if dic[d]==5:
        check= True

if check:
    print("YES")
else:
    print("NO")