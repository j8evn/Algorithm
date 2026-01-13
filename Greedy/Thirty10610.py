N= list(input())
if '0' not in N:
    print(-1)
else:
    ss= 0
    for i in range(len(N)):
        ss += int(N[i])
    if ss%3!=0:
        print(-1)
    else:
        N.sort(reverse=True)
        print(''.join(N))