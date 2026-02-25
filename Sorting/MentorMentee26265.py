import sys
input= sys.stdin.readline

N= int(input())
ll= []
for _ in range(N):
    ll.append(list(input().split()))
ll.sort(key= lambda x: x[1], reverse= True)
ll.sort(key= lambda x: x[0])

for a, b in ll:
    print(a, b)