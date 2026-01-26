N= int(input())
L= list(map(int, input().split()))
mm= 0
for i in range(N-1, 0, -1):
    if L[:i]==L[N-i:]:
        mm= i
        break
if mm==0:
    print("no")
else:
    print("yes")