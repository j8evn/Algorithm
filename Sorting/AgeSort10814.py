n= int(input())
List= []
for i in range(n):
    List.append(list(input().split()))
    List[i][0]= int(List[i][0])
List.sort(key=lambda x:x[0])
for i in range(n):
    List[i][0]= str(List[i][0])
    print(' '.join(List[i]))
