# 4. Tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []  # store all child nodes


class Tree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    # Add child node to specified parent node
    @staticmethod
    def add_child(parent_node, child_data):
        parent_node.children.append(TreeNode(child_data))

    # Level order traversal
    @staticmethod
    def level_order(node):
        res = []
        queue = [node]
        while queue:
            current = queue.pop(0)
            res.append(str(current.data))
            queue.extend(current.children)
        return " -> ".join(res)