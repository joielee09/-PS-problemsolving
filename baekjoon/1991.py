import sys
sys.stdin=open('input.txt')

n = int(sys.stdin.readline().strip())
tree={}

while n:
    n-=1
    root,left,right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

def preorder(root):
    if root!='.':
        sys.stdout.write(root)
        preorder(tree[root][0]) #left
        preorder(tree[root][1]) #right

def inorder(root):
    if root!='.':
        inorder(tree[root][0])
        sys.stdout.write(root)
        inorder(tree[root][1])

def postorder(root):
    if root!='.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        sys.stdout.write(root)

preorder('A')
print()
inorder('A')
print()
postorder('A')