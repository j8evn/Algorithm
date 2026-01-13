import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))

# L[i] : A[0]~[i] 중에 최대값  : 어떤 A[j] 가 선택되었을 때 j 보다 왼쪽 거중 제일 큰 거 선택
#  R[i] : A[i] ~ A[N-1] 중에 최대값
# L[i]의 경우 왼쪽일수록 많이 뺌 : N이 오른쪽에 있을 때를 예상
# 보상 : A[i]도 위치에 비례해서 -가 되었기 때문에 그만큼 보상

L, R = [0]*N, [0]*N
tt = -(N-1)*K
L[0] = -A[0] + tt
for i in range(1, N):
	tt += K
	L[i] = max(-A[i]+tt, L[i-1])

tt = -(N-1)*K
R[N-1] = -A[N-1] + tt
for i in range(N-2, -1, -1):
	tt += K
	R[i] = max(-A[i]+tt, R[i+1])

# 양쪽 끝은 보상이 좀 다름. 귀찮으니 그냥 따로 계산
mm = max(A[0]+ R[1], A[N-1]+L[N-2])


cp = (N-2)*K
for i in range(1, N-1):
	tt = A[i]+ L[i-1] + cp
	mm = max(mm, tt)
#	print(A[i], A[i]+ L[i-1], tt)
	cp = cp-K

cp = (N-2)*K
for i in range(N-2, 0, -1):
	tt = A[i]+ R[i+1] + cp
	mm = max(mm, tt)
#	print(A[i], A[i]+ R[i+1], tt)
	cp = cp-K

print(mm)
