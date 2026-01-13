N=int(input())
A= []
dic= {}
for i in range(N):
    A.append(int(input()))
    if A[i] in dic:
        dic[A[i]] += 1
    else:
        dic[A[i]]= 1
A.sort()
ll= [(k,v) for k, v in dic.items()]
ll.sort(key=lambda x:x[0])
ll.sort(key=lambda x:-x[1])

R= []
rr= sum(A)/N
if (rr-sum(A)//N)*10 >= 5:
    rr= sum(A)//N+ 1
else:
    rr= sum(A)//N
R.append(rr)
R.append(A[N//2])
if len(ll)>1 and ll[0][1]==ll[1][1]:
    R.append(ll[1][0])
else:
    R.append(ll[0][0])
R.append(A[-1]-A[0])

R= map(str,R)
print('\n'.join(R))