S= []
for i in range(8):
    k= int(input())
    S.append([k,i])
S.sort(key=lambda x:-x[0])
t= 0
R= []
for i in range(5):
    t += S[i][0]
    R.append(S[i][1]+1)
R.sort()
R= map(str,R)
print(t)
print(' '.join(R))