N= int(input())
V= input().strip()
a, b= 0, 0
for i in range(N):
  if V[i]=='A':
    a += 1
  else:
    b += 1

if a>b:
  print('A')
elif b>a:
  print('B')
else:
  print('Tie')