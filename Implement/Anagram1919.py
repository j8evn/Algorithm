a= input().strip()
b= input().strip()
A, B= [0]*26, [0]*26
for i in range(len(a)):
  A[ord(a[i])-ord('a')] += 1
for i in range(len(b)):
  B[ord(b[i])-ord('a')] += 1

cnt= 0
for i in range(26):
  if A[i]!=B[i]:
    cnt += (abs(A[i]-B[i]))
print(cnt)