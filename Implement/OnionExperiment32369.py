N, A, B= map(int,input().split())
o1, o2= 1, 1
for _ in range(N):
    o1 += A
    o2 += B
    if o1<o2:
        o1, o2= o2, o1
    elif o1==o2:
        o2= o2-1
print(o1, o2)