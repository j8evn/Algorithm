import sys
input = sys.stdin.readline
R =[]
while True:
	line = input()
	if not line:
		break
	a, b = map(int, line.split())
	R.append(a+b)
R = list(map(str, R))
print('\n'.join(R))