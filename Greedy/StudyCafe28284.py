N,M=map(int,input().split())
S,T=[0],[0]

#최대를 구하기 위해 큰 것부터 누적합을 구해놓음
A=list(map(int,input().split()))
A.sort()
for i in range(N):
    T.append(T[-1]+A[i])

#최소를 구하기 위해 작은 것부터 누적합을 구해놓음
A.reverse()
for i in range(N):
    S.append(S[-1]+A[i])
off,on=1,2
B=[]

#e+1로 해야함 ((s,e)에서 e도 포함)
for i in range(M):
    s,e=map(int,input().split())
    B.append([s,on])
    B.append([e+1,off])

#Event들을 시간 스탬프로 정렬, s를 만나면 cnt+1 e를 만나면 -1
B.sort()
cnt=0
ss1,ss2=0,0
pre=0
for i in range(0,len(B)):
#   print("TT", B[i][0], cnt, S[cnt], T[cnt], B[i][0] -pre, S[cnt]*(B[i][0] - pre))
# 이전 구간에서의 cnt와 구간의 길이를 곱하여 누적함
    ss1=ss1+S[cnt]*(B[i][0]-pre)
    ss2=ss2+T[cnt]*(B[i][0]-pre)
    pre=B[i][0]
    if (B[i][1]==on):
        cnt+=1
    else:
        cnt-=1
print(ss2,ss1)
