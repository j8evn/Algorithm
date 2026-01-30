import sys
input= sys.stdin.readline

def parentheses(S):
    mapping = {')':'(', ']':'[', '}':'{'}
    stack = []
    for s in S:
        if s=='(' or s=='[' or s=='{':
            stack.append(s)
        else:
            if not stack or stack[-1] != mapping[s]:
                return False
            stack.pop()
    if stack:
        return False
    return True

N= int(input())
for _ in range(N):
    S= input().rstrip()

    if parentheses(S):
        print("YES 0")
        continue
    
    ll= ['(', ')', '[', ']', '{', '}']
    found= False
    S_list= list(S)
    for i in range(len(S_list)):
        for p in ll:
            S_list[i]= p
            if parentheses(''.join(S_list)):
                found= True
                change= [i+1, p]
                break
            S_list[i]= S[i]
        if found:
            break

    if found:
        print("YES 1")
        print(change[0], change[1])
    else:
        print("NO")