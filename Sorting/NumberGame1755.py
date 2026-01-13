A= ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
M, N= map(int,input().split())
S= []
for i in range(M,N+1):
    if len(str(i))==1:
        S.append([A[i],i])
    else:
        ss= A[int(str(i)[0])]+" "+A[int(str(i)[1])]
        S.append([ss,i])
S.sort(key=lambda x:x[0])

R, cnt= "", 1
for i in range(len(S)):
    R += str(S[i][1])+" "
    if cnt%10==0:
        R += '\n'
    cnt += 1
print(R)