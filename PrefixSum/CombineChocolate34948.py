N= int(input())
A= list(map(int, input().split()))
B= list(map(int, input().split()))
ll= []
for i in range(N):
    ll.append((A[i],B[i]))
ll.sort(key= lambda x: x[0])

ll.insert(0, (0,0))
for i in range(N):
    ll[i+1]= (ll[i+1][0], ll[i+1][1]+ ll[i][1])

mm= 0
for i in range(1,N+1):
    if ll[i-1][0]==ll[i][0]:
        continue
    mm= max(mm, ll[i][0]*(ll[N][1]-ll[i-1][1]))
print(mm)