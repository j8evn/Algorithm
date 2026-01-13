k=['c=','c-','dz=','d-','lj','nj','s=','z=']
s=input().strip()
for i in k:
    s=s.replace(i,'*') # k의 원소를 *로 치환
print(len(s))
