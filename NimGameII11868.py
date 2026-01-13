# 백준 11868
# 스프라그-그런디?
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
acc = 0
for i in range(N):
	acc = acc ^ A[i]
if (acc !=0):
	print('koosaga')
else:
	print('cubelover')