Price = [350.34, 230.90, 190.55, 125.30, 180.90]

N = int(input())
for _ in range(N):
	A = list(map(int, input().split()))
	s = 0
	for i in range(5):
		s += A[i]*Price[i]
#	print(s)
	print("$"+ "{:.2f}".format(s))