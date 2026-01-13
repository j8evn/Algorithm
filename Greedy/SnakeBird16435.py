N, L= map(int,input().split())
H= list(map(int,input().split()))
H.sort()
for i in range(N):
  if L<H[i]:
    break
  L += 1
print(L)