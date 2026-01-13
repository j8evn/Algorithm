def Proc(a,b,c):
	t= [False]* mask
	cnt= 0
	while True:
		a= (a*b) % mask
		cnt += 1
		if a==c:
			return cnt
		if t[a]==True:
			return "NIKAD"
		t[a]= True

a, b, c= map(int, input().split())
mask = 10**len(str(c))
print(Proc(a,b,c))