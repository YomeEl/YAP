"""TreeWork7. Дано бинарное дерево и корень дерева P1. Необходимо вывести
минимальное значение в дереве. Решение должно иметь сложность по времени
исполнения T(n) = O(log(n)), где n - число вершин в дереве."""

from bin_tree import parse_bin_tree
from helpers import Helpers

if __name__ == "__main__":
    promt = "Выберите режим работы"
    variants = [("Ввод с клавиатуры", True), ("Использовать шаблон", False)]
    is_manual = Helpers.input_select(promt, variants)

    if is_manual:
        tree = Helpers.read_tree()
    else:
        tree = parse_bin_tree("4(2(1, 3), 5(6,))")

    print(f"Дерево P: {tree}")
    print(f"Минимальное значение в дереве: {tree.find_min_value()}")
