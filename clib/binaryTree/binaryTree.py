class TreeNode:
    def __init__(self, v, left=None, right=None) -> None:
        self.v = v
        self.left = left
        self.right = right

def insertNode(root: "TreeNode", node: "TreeNode"):
    """给你一个树的根节点，再给一个值，把node放在树合适的位置，返回一棵完整的树"""
    if root is None:
        root = node
    elif root.v > node.v:
        ltree = insertNode(root.left, node)
        root.left = ltree
    elif root.v < node.v:
        rtree = insertNode(root.right, node)
        root.left = rtree
    return root

def deleteNode(root: TreeNode, node: TreeNode):
    pass