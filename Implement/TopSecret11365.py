while True:
  ss= input()
  if ss=='END':
    break
  ans= ""
  for i in range(len(ss)-1,-1,-1):
    ans += ss[i]
  print(ans)