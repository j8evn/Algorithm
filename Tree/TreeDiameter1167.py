import sys
input = sys.stdin.readline

def bfs(n):
	V= [False]*N
	D[n], V[n] =0, True
	fr, re =0, 0
	que[re], re = n, re+1
	while (fr != re):
		t, fr = que[fr], fr+1
		for e in G[t] :
			if (V[e] == True):
				continue
			D[e] = D[t]+G[t][e]
			que[re], re = e, re+1
			V[e] = True

N = int(input())
G =[]
for i in range(N):
	G.append({})
for i in range(N):
	a = list(map(int, input().split()))
	n = a[0]-1
	for j in range(1, len(a)-1, 2):
		t= a[j]-1
		G[n][t] = a[j+1]

#print(G)
que =[-1]*N
D =[0]*N
bfs(0)
far, mm = -1, -1
for i in range(N):
	if (D[i]>mm):
		far, mm = i, D[i]
D=[0]*N
bfs(far)
print(max(D))