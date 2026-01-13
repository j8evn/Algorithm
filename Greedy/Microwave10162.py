T= int(input())

if T%10==0:
    abc= [300, 60, 10]
    ABC= [0, 0, 0]
    for i in range(3):
        ABC[i]= T//abc[i]
        T= T%abc[i]
    ABC= map(str,ABC)
    print(' '.join(ABC))

else:
    print(-1)
        
