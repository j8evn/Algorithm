T= int(input())
for _ in range(T):
  A= list(map(int,input().split()))
  k= A.pop(0)
  cnt= 0
  for i in range(20):
    for j in range(0, 20-1):
      if (A[j] > A[j+1]):
        A[j], A[j+1]= A[j+1], A[j]
        cnt += 1
  print(k,cnt)