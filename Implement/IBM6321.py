n= int(input())
for i in range(n):
    ss= input().strip()
    new= ""
    print("String #%d"%(i+1))
    for j in range(len(ss)):
        new= new+ chr((ord(ss[j])+1-ord('A'))%26+ord('A'))
    print(new+"\n")
