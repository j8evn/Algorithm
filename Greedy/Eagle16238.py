N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
ss= 0
for i in range(N):
   tt = A[i] - i
   if (tt <=0):
      break
   ss += tt
print(ss)
