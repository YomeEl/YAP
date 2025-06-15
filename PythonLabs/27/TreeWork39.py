"""TreeWork39. Дан корень дерева, хранящего арифметическое выражение. В выражении
участвуют неотрицательные однозначные целые числа, знаки операций кодируются
отрицательными числами: сложению соответствует -1, вычитанию -2, умножению-3, делению-4.
Создать копию этого дерева и в созданной копии заменить все выражения вида:
0*a, a*0, 0/a, a-a на 0. Учесть, что в качестве a может быть выражение.
Если в результате одного преобразования дерева вновь появляются выражения данного вида,
их также нужно преобразовывать и в результирующем дереве таких выражений быть не должно.
Вывести указатель на корень дерева, полученного в результате, и полученное арифметическое
выражение в виде строки символов"""

from helpers import Helpers


class ExpressionTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        if self.value >= 0:
            return str(self.value)

        left = "" if not self.left else str(self.left)
        right = "" if not self.right else str(self.right)
        match self.value:
            case -1:
                value = "+"
            case -2:
                value = "-"
            case -3:
                value = "*"
            case -4:
                value = "/"
            case _:
                value = str(self.value)

        if len(left) > 1:
            left = f"({left})"
        if len(right) > 1:
            right = f"({right})"

        return f"{left} {value} {right}"

    def copy(self):
        return self.__copy(self)

    def __copy(self, root):
        if root is None:
            return None
        new_node = ExpressionTreeNode(root.value)
        new_node.left = self.__copy(root.left)
        new_node.right = self.__copy(root.right)
        return new_node


class ExpressionTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def parse(self, string):
        self.root = self.__parse_node(string)

    def simplify(self):
        self.__simplify(self.root)

    def copy(self):
        new_tree = ExpressionTree()
        new_tree.root = self.root.copy()
        return new_tree

    def __simplify(self, root: ExpressionTreeNode):
        if root is None:
            return

        self.__simplify(root.left)
        self.__simplify(root.right)

        should_simplify = False
        if root.value == -3:
            if root.left.value == 0 or root.right.value == 0:
                should_simplify = True
        if root.value == -4 and root.left.value == 0:
            should_simplify = True
        if root.value == -2 and root.left.value == root.right.value:
            should_simplify = True

        if should_simplify:
            root.value = 0
            root.left = None
            root.right = None

    def __remove_redundant_parens(self, string: str):
        if string[0] != "(" and string[:-1] != ")":
            return string

        length = len(string)
        balance = 0
        for i, char in enumerate(string):
            if char == "(":
                balance = balance + 1
            elif char == ")":
                balance = balance - 1
                if balance == 0 and i != length - 1:
                    return string
        return string[1:-1]

    def __parse_node(self, string):
        OPS = ["+", "-", "*", "/"]

        def order(operator):
            if operator in ["+", "-"]:
                return 1
            if operator in ["*", "/"]:
                return 2

        def convert(char):
            if char in OPS:
                return -(OPS.index(char) + 1)
            return int(char)

        string = self.__remove_redundant_parens(string)

        lowest_op_index = -1
        lowest_op_order = 3
        lowest_op_balance = 999
        balance = 0
        for i, char in enumerate(string):
            if char == "(":
                balance = balance + 1
            elif char == ")":
                balance = balance - 1
            elif char == " ":
                continue
            elif char in OPS:
                cur_order = order(char)
                if balance <= lowest_op_balance:
                    if balance == lowest_op_balance and cur_order > lowest_op_order:
                        continue
                    lowest_op_index = i
                    lowest_op_order = cur_order
                    lowest_op_balance = balance

        if lowest_op_index == -1:
            return ExpressionTreeNode(convert(string))

        node = ExpressionTreeNode(convert(string[lowest_op_index]))

        node.left = self.__parse_node(string[:lowest_op_index])
        node.right = self.__parse_node(string[lowest_op_index + 1 :])
        return node


def run_test():
    expr = "(2-(0*1+2))+4"
    print(f"Исходное выражение: {expr}")

    tree = ExpressionTree()
    tree.parse(expr)
    copy = tree.copy()
    copy.simplify()

    print(f"Результат: {copy}")
    print(f"Исходное дерево: {tree}")


def run_manual():
    promt = "Введите выражение: "

    def converter(string):
        tree = ExpressionTree()
        tree.parse(string)
        return tree

    condition = lambda _: True
    tree = Helpers.input_with_condition(promt, "", converter, condition)
    copy = tree.copy()
    copy.simplify()

    print(f"Результат: {copy}")
    print(f"Исходное дерево: {tree}")


if __name__ == "__main__":
    promt = "Выберите режим работы"
    variants = [("Ввод с клавиатуры", True), ("Запустить тесты", False)]
    is_manual = Helpers.input_select(promt, variants)

    if is_manual:
        run_manual()
    else:
        run_test()
