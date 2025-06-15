"""TreeWork26. Дано дерево поиска и корень дерева P1. Удалить в дереве корневую
вершину. При замене содержимого удаляемой вершины использовать данные из ее левого
поддерева. После удаления вывести строку с описанием исходного дерева в следующем
формате:
    <дерево> ::= ((<левое поддерево>)<вершина>(<правое поддерево>))
               | ((<левое поддерево>)<вершина>)
               | (<вершина>(<правое поддерево>))
    <вершина> ::= <цифра><цифра> | <цифра>
    <левое поддерево> ::= <дерево>
    <правое поддерево> ::= <дерево>
Например, "(((1)2((3)4))5(6(7)))".
Пробелы в результирующей строке отсутствуют, ссылки на пустые деревья никак не выводятся.
"""

from bin_tree import TreeNode, BinTree
from helpers import Helpers


class BinTreeParser:
    def __init__(self):
        pass

    def parse(self, string):
        node = self.__parse_node(string)
        tree = BinTree()
        tree.root = node
        return tree

    def __parse_node(self, string):
        if string == "":
            return None
        open_index = None
        balance = 0
        value_string = ""
        left_subtree = ""
        right_subtree = ""
        for i, char in enumerate(string):
            if char == "(":
                if balance == 1:
                    open_index = i
                balance = balance + 1
            elif char == ")":
                balance = balance - 1
                if balance == 1:
                    subtree = string[open_index : i + 1]
                    if value_string == "":
                        left_subtree = subtree
                    else:
                        right_subtree = subtree
            elif balance == 1:
                value_string = value_string + char

        node = TreeNode(int(value_string))
        node.left = self.__parse_node(left_subtree)
        node.right = self.__parse_node(right_subtree)
        return node


def test(name, tree_string, expect):
    print("====")
    print(f"TEST DESCRIPTION\n\t{name}")
    print(f"INPUT\n\t{tree_string}")
    print(f"EXPECTED RESULT\n\t{expect}")

    parser = BinTreeParser()
    tree = parser.parse(tree_string)
    tree.remove_root()

    print(f"ACTUAL RESULT\n\t{tree}")
    print("TEST RESULT")
    print("\tSUCCESS" if str(tree) == expect else "\tERROR")
    print("====")


def run_test():
    test("No left subtree", "(2((4)3(5)))", "((4)3(5))")
    test("No right subtree", "(((4)3(5))2)", "((4)3(5))")
    test("No right subtree in left subtree", "(((1)2)3((5)6(7)))", "((1)2((5)6(7)))")
    test("Full tree of height 2", "(((1)2(3))4((5)6(7)))", "((1)2(((3)5)6(7)))")


def run_manual():
    print("<дерево> ::= ((<левое поддерево>)<вершина>(<правое поддерево>))")
    print("           | ((<левое поддерево>)<вершина>)")
    print("           | (<вершина>(<правое поддерево>))")
    print("<левое поддерево> ::= <дерево>")
    print("<правое поддерево> ::= <дерево>")

    promt = "Введите <дерево>: "

    def converter(string):
        parser = BinTreeParser()
        return parser.parse(string)

    condition = lambda _: True
    tree = Helpers.input_with_condition(promt, "", converter, condition)
    tree.remove_root()
    print(f"Дерево после удаления корня: {tree}")


if __name__ == "__main__":
    promt = "Выберите режим работы"
    variants = [("Ввод с клавиатуры", True), ("Запустить тесты", False)]
    is_manual = Helpers.input_select(promt, variants)

    if is_manual:
        run_manual()
    else:
        run_test()
