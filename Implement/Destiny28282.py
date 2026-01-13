import sys
input=sys.stdin.readline

X, K = map(int, input().split()) # 양말의 개수, 양말 색의 가짓수
A = list(map(int, input().split())) # 양말 색의 번호
L, R = [0]*K, [0]*K # 오른쪽 양말, 왼쪽 양말
for i in range(X):
	L[A[i]-1] +=1 # L리스트에 해당 색상의 개수를 증가시킴
for i in range(X, X*2):
	R[A[i]-1] +=1 # R리스트에 해당 색상의 개수를 증가시킴
cnt = 0
for i in range(K):
	if (L[i] == 0): # 한 색의 가짓수가 0이면 continue
		continue
	cnt += L[i]*(X-R[i]) # 경우의 수: (한 색의 가짓수)*(나머지 색의 가짓수)
print(cnt)
