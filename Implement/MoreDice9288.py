T= int(input())
for t in range(T):
    N= int(input())
    print('Case {}:'.format(t+1))
    for i in range(1,7):
        for j in range(i,7):
            if i+j==N:
                print('({},{})'.format(i,j))