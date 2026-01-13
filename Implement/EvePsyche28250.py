import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
zero, one, others = 0, 0, 0
for i in range(N):
	if (A[i] ==0):
		zero +=1
	elif (A[i] ==1):
		one +=1
	else:
		others +=1
t1 = zero*(zero-1) //2		# {0,0} -> 1
t2 = zero * one	*2		# {0,1} -> 2
t3 = zero * others		# {0, others} -> 1
				# {nonzero, nonzero} -> 0
print(t1+t2+t3)
