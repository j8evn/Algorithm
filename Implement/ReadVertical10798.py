A,L=[],-1 # L: 가장 긴 문자열의 길이를 담을 변수
for i in range(5):
    A.append(input().strip())
    L=max(L,len(A[-1])) # 새로 추가될 때마다 기존 L과 비교 -> 더 큰 값 들어옴.
R=[] 
for i in range(L):
    for j in range(5):
        if (i>=len(A[j])): # for루프가 최대 길이만큼 돌도록 되어있기 때문에 그 보다 작은 값에서 continue
            continue
        else:
            R.append(A[j][i])
print(''.join(R))
