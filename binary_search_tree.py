# 5. Binary Search Tree
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None # left subtree
        self.right = None # right subtree

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert data
    def insert(self, data):
        if not self.root:
            self.root = BSTNode(data)
        else:
            self._insert_recursive(self.root, data)

    # Recursive helper function for insertion
    def _insert_recursive(self, node, data):
        if data < node.data:
            if not node.left:
                node.left = BSTNode(data)
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if not node.right:
                node.right = BSTNode(data)
            else:
                self._insert_recursive(node.right, data)

    # In-order traversal (ascending order)
    def inorder(self, node, res=None):
        if res is None:
            res = []
        if node:
            self.inorder(node.left, res)
            res.append(str(node.data))
            self.inorder(node.right, res)
        return " -> ".join(res)