import collections
from objprint import op as me

class Node:
    def __init__(self, val, left=None, right=None, parent=None) -> None:
        self.val = val
        self.parent = parent
        self.right = right
        self.left = left
    def __repr__(self) -> str:
        return self.val


def print_BST(root):
    res = []
    q = collections.deque()
    q.appendleft(root)
    while q:
        size = len(q)  # 这一层的节点个数
        layer = []
        for i in range(size):
            tmp_n: Node = q.pop()
            if tmp_n.val == '*':
                layer.append(tmp_n.val)
                continue
            if tmp_n.left:
                q.appendleft(tmp_n.left)
            else:
                q.appendleft(Node('*'))
            if tmp_n.right:
                q.appendleft(tmp_n.right)
            else:
                q.appendleft(Node('*'))
            layer.append(tmp_n.val)
        res.append(layer)
        layer = []
    for line_id in range(len(res)):
        print(' '*(len(res)-line_id) , ' '.join(list(map(str, res[line_id]))))

def insertNode(root, node):
    # 函数作用: 把这个节点node插入到树tree合适的位置上，并返回这棵树的根节点   
    if root is None:
        root = node
    elif root.val > node.val:
        lc = insertNode(root.left, node)
        lc.parent = root
        root.left = lc
    elif root.val < node.val:
        rc = insertNode(root.right, node)
        rc.parent = root
        root.right = rc
    return root

if __name__ == '__main__':

    n = Node(7)
    n1 = Node(5)
    n2 = Node(9)
    n3 = Node(1)
    n4 = Node(6)
    for ni in [n1, n2, n3, n4]:
        insertNode(n, ni)
    print_BST(n)



