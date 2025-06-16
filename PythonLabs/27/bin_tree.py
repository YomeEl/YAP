class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        left = "" if not self.left else str(self.left)
        right = "" if not self.right else str(self.right)
        return f"({left}{self.value}{right})"
    
    def update_height(self):
        if self.left: 
            self.left.update_height()
            left_height = self.left.height
        else:
            left_height = 0

        if self.right: 
            self.right.update_height()
            right_height = self.right.height
        else:
            right_height = 0

        self.height = 1 + max(left_height, right_height)

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
        self.__insert_node(free_node)

    def insert(self, value):
        node = TreeNode(value)
        if self.root is None:
            self.root = node
        else:
            self.__insert_node(TreeNode(value))

    def update_heights(self):
        if self.root is None: return
        self.root.update_height()

    def balance(self):
        self.update_heights()
        self.__balance(self.root, None)

    def __rotate_ll(self, node, parent):
        is_root = parent is None 
        if not is_root: is_left = parent.left == node

        lr = node.left.right
        new_root = node.left

        new_root.right = node
        new_root.right.left = lr

        if is_root:
            self.root = new_root
        elif is_left:
            parent.left = new_root
        else:
            parent.right = new_root


    def __balance(self, node, parent):
        if node is None: return
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        balance = left_height - right_height
        if balance > 1:
            self.__rotate_ll(node, parent)
            return
        
        self.__balance(node.left, node)
        self.__balance(node.right, node)

    def __find_ll_imbalance(self, parent_node, node):
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        balance = left_height - right_height
        if balance == 2:
            return (parent_node, node)
        left_result = self.__find_ll_imbalance(node, node.left)
        right_result = self.__find_ll_imbalance(node, node.right)


    def __insert_node(self, node):
        parent = None
        next_parent = self.root
        while next_parent:
            parent = next_parent
            next_parent = parent.left if node.value <= parent.value else parent.right
        if node.value <= parent.value:
            parent.left = node
        else:
            parent.right = node

def print_tree(tree: BinTree, prefix = ""):
    tree.update_heights()
    root = tree.root
    nodes = []
    __collect(root, 0, nodes)
    
    lines = [[] for _ in range(root.height)]
    for node, level in nodes:
        for i, line in enumerate(lines):
            line.append(str(node) if i == level else " ")
    for line in lines:
        print(prefix + " ".join(line)) 

def __collect(node, level, acc):
    if node.left: __collect(node.left, level + 1, acc)
    acc.append((node.value, level))
    if node.right: __collect(node.right, level + 1, acc)
