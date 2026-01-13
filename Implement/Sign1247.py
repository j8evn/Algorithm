for _ in range(3):
  n= int(input())
  S=[]
  for i in range(n):
    S.append(int(input()))
  if sum(S)==0:
    print(0)
  elif sum(S)<0:
    print("-")
  else:
    print("+")