def Go(l, r):
	global dp
	if (l >= r):
		return 0
	mm = -1
	if (dp[l][r] != -1):
		return dp[l][r]
	if ((S[l] == 'a') and (S[r]=='t')):
		mm = max(mm, Go(l+1, r-1)+2)
	if ((S[l] == 'g') and (S[r]=='c')):
		mm = max(mm, Go(l+1, r-1)+2)
	for i in range(l, r):
		mm = max(mm, Go(l,i)+Go(i+1, r))
	dp[l][r] = mm
	return mm

S = input().strip()
N = len(S)+1
dp =[]
for i in range(N):
	dp.append([-1]*N)
print(Go(0, len(S)-1))
