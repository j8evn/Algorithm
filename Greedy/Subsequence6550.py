import sys
input = sys.stdin.readline

while True:
	line = input()
	if not line:
		break
	s, t= line.split()
	j= 0
	for i in range(len(t)):
		if j < len(s) and s[j] == t[i]:
			j += 1
	if j == len(s):
		print("Yes")
	else:
		print("No")