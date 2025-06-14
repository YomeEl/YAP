"""TreeWork17. Дано бинарное дерево и корень дерева P1. Необходимо вывести второе
минимальное значение в дереве. Решение должно иметь сложность по времени
исполнения T(n) = O(log n), где n - число вершин в дереве."""

from bin_tree import parse_bin_tree
from helpers import Helpers

if __name__ == "__main__":
    promt = "Выберите режим работы"
    variants = [("Ввод с клавиатуры", True), ("Использовать шаблон", False)]
    is_manual = Helpers.input_select(promt, variants)

    if is_manual:
        tree = Helpers.read_tree()
    else:
        tree = parse_bin_tree("7(3(1(,1),5(4,6)),9(8,10))")

    print(f"Дерево P: {tree}")
    result = tree.find_second_to_last_min_value()
    print(
        f"Второе минимальное значение в дереве: {result if result else "не найдено!"}"
    )
