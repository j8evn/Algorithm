import sys

while True:
    N= sys.stdin.readline() # 무한루프 여러줄 입력받을때
    if not N:
        break # 다음 줄 없으면 break
    A=[0, 0, 0, 0]
    for i in range(len(N)):
        if ord('a')<=ord(N[i]) and ord(N[i])<=ord('z'):
            A[0]+= 1
        elif ord('A')<=ord(N[i]) and ord(N[i])<=ord('Z'):
            A[1]+= 1
        elif ord('0')<=ord(N[i]) and ord(N[i])<=ord('9'):
            A[2]+= 1
        elif ord(' ')==ord(N[i]):
            A[3]+= 1
    A= map(str,A)
    print(' '.join(A))
