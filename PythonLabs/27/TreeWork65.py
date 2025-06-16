"""TreeWork65. В первой строке текстового файла записаны целые числа, разделенные
пробелами. Создать дерево поиска, последовательно включая в него перечисленные в файле
числа. После этого необходимо, привести дерево к АВЛ-сбалансированному виду, выполнив для
LL-поворот. Известно, что требуется не более одного такого поворота.
Вывести корень полученного дерева."""

# examples 
#   (((2)5)10) -> ((2)5(10))
#   ((((1)2)3)4(5(6))) -> (((1)2(3))4(5(6)))
#   ((((1)2(3))4)5(6(7))) -> (((1)2((3)4))5(6(7)))

from helpers import Helpers
from TreeWork26 import BinTreeParser
from bin_tree import print_tree

def test(name, tree_string, expect):
    print("====")
    print(f"INPUT\n\t{tree_string}")

    parser = BinTreeParser()
    tree = parser.parse(tree_string)
    print_tree(tree, "\t")
    tree.balance()

    print(f"EXPECTED RESULT\n\t{expect}")
    print(f"ACTUAL RESULT\n\t{tree}")
    print_tree(tree, "\t")
    print("TEST RESULT")
    print("\tSUCCESS" if str(tree) == expect else "\tERROR")
    print("====")


def run_test():
    test("No left subtree", "(((2)5)10)", "((2)5(10))")
    test("No right subtree", "((((1)2)3)4(5(6)))", "(((1)2(3))4(5(6)))")
    test("No right subtree in left subtree", "((((1)2(3))4)5(6(7)))", "(((1)2((3)4))5(6(7)))")


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
    tree.balance()
    print(f"Дерево после балансировки LL-поворотом: {tree}")


if __name__ == "__main__":
    promt = "Выберите режим работы"
    variants = [("Ввод с клавиатуры", True), ("Запустить тесты", False)]
    is_manual = Helpers.input_select(promt, variants)

    if is_manual:
        run_manual()
    else:
        run_test()
