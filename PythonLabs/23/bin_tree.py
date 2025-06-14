class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        if self is None:
            return "_"
        children_string = ""
        if self.left or self.right:
            children_string = f"({self.left}, {self.right})"
        return f"{self.value}{children_string}"


class BinTree:
    def __init__(self):
        self.root = None
        pass

    def __str__(self):
        return str(self.root)

    def find_min_value(self):
        return BinTree.__find_min_rec(self.root)

    def insert(self, value):
        node = TreeNode(value)
        if self.root is None:
            self.root = node
            return

        parent_node = self.root
        while True:
            if value < parent_node.value:
                new_parent = parent_node.left
                if new_parent is None:
                    parent_node.left = node
                    return
            else:
                new_parent = parent_node.right
                if new_parent is None:
                    parent_node.right = node
                    return
            parent_node = new_parent

    def get_sorted_values(self):
        return BinTree.__get_values_rec(self.root)

    def find_second_to_last_min_value(self):
        node, is_found = BinTree.__find_second_min_rec(self.root)
        return node.value if is_found else None

    @staticmethod
    def __find_min_rec(node: TreeNode | None):
        if node.left:
            return BinTree.__find_min_rec(node.left)
        return node.value

    @staticmethod
    def __find_second_min_rec(node: TreeNode):
        if node is None:
            return (None, False)

        if node.left:
            min_node, is_found = BinTree.__find_second_min_rec(node.left)
            if is_found:
                return (min_node, True)
            if node.value > min_node.value:
                return (node, True)
            else:
                return (min_node, False)

        return (node, False)

    @staticmethod
    def __get_values_rec(node):
        if node is None:
            return []
        left_values = BinTree.__get_values_rec(node.left)
        right_values = BinTree.__get_values_rec(node.right)
        node_value = [node.value]
        return left_values + node_value + right_values


def __parse_node(node_string):
    if node_string == "":
        return None

    open_index = None
    close_index = None
    separator_index = None
    balance = 0
    for i, char in enumerate(node_string):
        if char == "(":
            balance = balance + 1
            if open_index is None:
                open_index = i
        if char == "," and balance == 1:
            if separator_index is not None:
                return None
            separator_index = i
        if char == ")":
            balance = balance - 1
            close_index = i

    if open_index is None:
        value_string = node_string
    else:
        value_string = node_string[:open_index]
    node = TreeNode(int(value_string))

    if not open_index is None:
        node.left = __parse_node(node_string[open_index + 1 : separator_index])
        node.right = __parse_node(node_string[separator_index + 1 : close_index])

    return node


def parse_bin_tree(tree_string):
    tree = BinTree()
    tree.root = __parse_node(tree_string)
    return tree
