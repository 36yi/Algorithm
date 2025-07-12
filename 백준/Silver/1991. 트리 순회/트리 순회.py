import sys
input =sys.stdin.readline
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self, val, x = None, y= None):
        self.val = val
        self.left = x
        self.right = y

N = int(input())
li = []
for i in range(N):
    li.append(Node(chr(i+65)))

for i in range(N):
    a,b,c = input().split()
    if b != '.':
        li[ord(a)-65].left = li[ord(b) - 65]
    if c != '.':
        li[ord(a)-65].right = li[ord(c) - 65]

def dfs(node):
    print(node.val,end="")
    if node.left:
        dfs(node.left)

    if node.right:
        dfs(node.right)

def dfs2(node):
    if node.left:
        dfs2(node.left)

    print(node.val,end="")

    if node.right:
        dfs2(node.right)
def dfs3(node):
    if node.left:
        dfs3(node.left)
    if node.right:
        dfs3(node.right)
    print(node.val,end="")

dfs(li[0])
print()
dfs2(li[0])
print()
dfs3(li[0])