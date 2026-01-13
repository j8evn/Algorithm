import sys
input= sys.stdin.readline

n= int(input())
for _ in range(n):
    A= list(input().split())
    if A[0]=='rectangle':
        if A[3]=='y':
            for i in range(int(A[1])):
                print("#"*int(A[2]))
        else:
            print("#"*int(A[2]))
            for _ in range(int(A[1])-2):
                print("#"+" "*(int(A[2])-2)+"#")
            print("#"*int(A[2]))
    elif A[0]=='left':
        if A[3]=='y':
            for i in range(int(A[2])):
                print("#"*(i+1))
        else:
            print("#")
            for i in range(int(A[2])-2):
                print("#"+" "*i+"#")
            print("#"*int(A[2]))
    elif A[0]=='right':
        if A[3]=='y':
            for i in range(int(A[2])):
                print(" "*(int(A[2])-i-1)+"#"*(i+1))
        else:
            print(" "*(int(A[2])-1)+"#")
            for i in range(int(A[2])-2):
                print(" "*(int(A[2])-i-2)+"#"+" "*(i)+"#")
            print("#"*int(A[2]))
    else:
        if A[2]=='y':
            for i in range(int(A[1])//2+1):
                print(" "*(int(A[1])//2-i)+"#"*(2*i+1))
            for i in range(int(A[1])//2-1,-1,-1):
                print(" "*(int(A[1])//2-i)+"#"*(2*i+1))
        else:
            print(" "*(int(A[1])//2)+"#")
            for i in range(1,int(A[1])//2+1):
                print(" "*(int(A[1])//2-i)+"#"+" "*(2*i-1)+"#")
            for i in range(int(A[1])//2-1,0,-1):
                print(" "*(int(A[1])//2-i)+"#"+" "*(2*i-1)+"#")
            print(" "*(int(A[1])//2)+"#")