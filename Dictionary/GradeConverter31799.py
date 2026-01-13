import sys
input= sys.stdin.readline
'''
N= int(input())
S= input().strip()
ll= len(S)

S= S+"0"
A= []
fix= set(list("+-0"))
loc= 0
while(loc<ll):
    if((S[loc+1] in fix)==False):
        A.append(S[loc]+"0")
        loc= loc+ 1
    else:
        A.append(S[loc:loc+2])
        loc= loc+ 1
print(A)
gr= ["A+","A0","A-","B+","B0","B-","C+","C0","C-"]
gr.reverse()
dic={}
for i in range(9):
    dic[gr[i]]= i
for i in range(N):
    A[i]= dic[A[i]]

R=[]
for i in range(N):
    if(A[i]==dic["A+"]):
        R.append("E")
    elif(A[i]<=dic["C+"]):
        R.append("B")
    elif(A[i]<= dic["B0"]):
        if ((i==0) or (A[i-1] <= dic["C+"])):
            R.append("D")
        else: 
            R.append("B")
    elif (A[i]<= dic["A-"]):
        if ((i==0) or (A[i-1] <= dic["B0"])):
            R.append("P")
        else: 
            R.append("D")
    else:
        if ((i==0) or (A[i-1] <= dic["A-"])):
            R.append("E")
        else: 
            R.append("P")
print(''.join(R))
'''

N = int(input())
S = input().strip()
ll = len(S)
# 일단 0을 붙여놓고 필요시에만 쓰면 된다. 원래의 길이는 ll에 저장
S = S+"0"
A=[]
loc = 0
fix = set(list("+-0"))
while (loc <ll):
# 다음의 문자가 +, -, 0가 아니면 0을 붙임. 하나만 전진
	if((S[loc+1] in fix) == False):
		A.append(S[loc]+"0")
		loc = loc+1
# 다음의 문자가 +, -, 0면 두 글자 전진
	else:
		A.append(S[loc:loc+2])
		loc = loc+2
#print(A)
gr =["A+", "A0", "A-","B+", "B0", "B-","C+", "C0", "C-"]
gr.reverse()
dic ={}
for i in range(9):
	dic[gr[i]]= i
for i in range(N):
	A[i] = dic[A[i]]

R=[]
for i in range(N):
	if (A[i] ==dic["A+"]):
		R.append("E")
	elif (A[i] <= dic["C+"]):
		R.append("B")
	elif (A[i]<= dic["B0"]):
		if ((i==0) or (A[i-1] <= dic["C+"])):
			R.append("D")
		else: 
			R.append("B")
	elif (A[i]<= dic["A-"]):
		if ((i==0) or (A[i-1] <= dic["B0"])):
			R.append("P")
		else: 
			R.append("D")
	else:
		if ((i==0) or (A[i-1] <= dic["A-"])):
			R.append("E")
		else: 
			R.append("P")
print(''.join(R))
