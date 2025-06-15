class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        left = "" if not self.left else str(self.left)
        right = "" if not self.right else str(self.right)
        return f"({left}{self.value}{right})"


class BinTree:
    def __init__(self):
        self.root = None
        pass

    def __str__(self):
        return str(self.root)

    def remove_root(self):
        if not self.root.left:
            self.root = self.root.right
            return

        root_right = self.root.right

        self.root = self.root.left
        if not root_right:
            return

        if not self.root.right:
            self.root.right = root_right
            return

        free_node = self.root.right
        self.root.right = root_right
        parent = None
        next_parent = self.root
        while next_parent:
            parent = next_parent
            next_parent = (
                parent.left if free_node.value <= parent.value else parent.right
            )
        if free_node.value <= parent.value:
            parent.left = free_node
        else:
            parent.right = free_node
