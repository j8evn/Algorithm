def preorder(n): # 전위순회 (DLR)
    if n==-1:
        return
    r1.append(Tree[n][0])
    preorder(Tree[n][1])
    preorder(Tree[n][2])

def inorder(n): # 중위순회 (LDR)
    if n==-1:
        return
    inorder(Tree[n][1])
    r2.append(Tree[n][0])
    inorder(Tree[n][2])

def postorder(n): # 후위순회 (LRD)
    if n==-1:
        return
    postorder(Tree[n][1])
    postorder(Tree[n][2])
    r3.append(Tree[n][0])

N= int(input())
Tree= []
r1, r2, r3= [], [], []
for i in range(N):
    Tree.append([chr(ord('A')+i),0,0])
for i in range(N):
    n1, n2, n3= input().split()
    if n2=='.':
        Tree[ord(n1)-ord('A')][1]= -1
    else:
        Tree[ord(n1)-ord('A')][1]= ord(n2)-ord('A')
    if n3=='.':
        Tree[ord(n1)-ord('A')][2]= -1
    else:
        Tree[ord(n1)-ord('A')][2]= ord(n3)-ord('A')

preorder(0)
print(''.join(r1))
inorder(0)
print(''.join(r2))
postorder(0)
print(''.join(r3))