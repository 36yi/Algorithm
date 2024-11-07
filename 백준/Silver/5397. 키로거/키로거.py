import sys
class Node:
    def __init__(self, value,left=None, right=None):
        self.left = None
        self.right = None
        self.value = value




t = int(input())
for _ in range(t):
    s = sys.stdin.readline().rstrip()
    head = node = Node(0)
    for c in s:
        if c == '<':
            if node.left == None:
                continue
            else:
                node = node.left

        elif c == '>':
            if node.right == None:
                continue
            else:
                node = node.right

        elif c == '-':
            if node.left == None:
                continue
            else:
                if node.right != None:
                    node.right.left = node.left

                node.left.right = node.right
                node = node.left

        else:
            value = c
            n = Node(value)
            if node.right != None:
                node.right.left = n
            n.left = node
            n.right = node.right
            node.right = n
            node = n

    head= head.right
    while head:
        print(head.value, end="")
        head = head.right
    print()
