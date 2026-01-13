h, m = map(int, input().split())
m = h*60 +m
m = m -45
if (m <0):
	m = m + 24*60
print(m//60, m%60)
