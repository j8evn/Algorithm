import sys
input= sys.stdin.readline

N= int(input())
ll= []
for _ in range(N):
  ss= input().strip()
  t= ""
  for i in range(len(ss)):
    if ord('0') <= ord(ss[i]) <= ord('9'):
      t += ss[i]
    elif ord('a') <= ord(ss[i]) <= ord('z'):
      if t:
        ll.append(int(t))
        t= ""
  if t:
    ll.append(int(t))

ll.sort()
ll= map(str,ll)
print('\n'.join(ll))