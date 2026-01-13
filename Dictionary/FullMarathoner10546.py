N= int(input())
dic= {}
for _ in range(N):
    s= input().strip()
    if s in dic:
        dic[s] += 1
    else:
        dic[s]= 1

for _ in range(N-1):
    s= input().strip()
    if s in dic:
        dic[s] -= 1

for d in dic:
    if dic[d]>0:
        print(d)