L= int(input())
S= list(map(int,input().split()))
n= int(input())
S.append(0)
S.sort()

m1, m2= 0, 0
for i in range(1,len(S)):
    if S[i-1]<n<S[i]:
        m1, m2= S[i-1], S[i]
        break
 
m1, m2= m1+1, m2-1
cnt= 0
for i in range(m1,m2+1):
    for j in range(i+1,m2+1):
        if i<=n<=j:
            cnt += 1
print(cnt)