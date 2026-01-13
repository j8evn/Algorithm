import sys
input= sys.stdin.readline

T= int(input())
for _ in range(T):
  J, N= map(int,input().split())
  A= []
  for _ in range(N):
    r, c= map(int,input().split())
    A.append(r*c)
  A.sort(reverse=True)
  cnt, i= 0, 0
  while J>0:
    cnt += 1
    J= J- A[i]
    i += 1
  print(cnt)