"""TreeWork16. Дано число N (> 0) и набор из N чисел. Отсортировать исходный
набор чисел, создав для него бинарное дерево. Вывести корень P1 полученного дерева,
а также отсортированный набор чисел (для вывода набора чисел выполнить перебор вершин
дерева в инфиксном порядке)."""

from bin_tree import BinTree
from helpers import Helpers

if __name__ == "__main__":
    n_promt = "Введите количество чисел N: "
    n_error = "Неверно введено количество!"
    n_condition = lambda n: n > 0
    n = Helpers.input_with_condition(n_promt, n_error, int, n_condition)

    arr_promt = f"Введите {n} чисел через пробел: "
    arr_error = "Введено неверное количество чисел!"
    arr_converter = lambda string: [i for i in map(int, string.rsplit())]
    arr_condition = lambda arr: len(arr) == n
    arr = Helpers.input_with_condition(
        arr_promt, arr_error, arr_converter, arr_condition
    )

    tree = BinTree()
    for number in arr:
        tree.insert(number)

    print(f"Корень дерева: {tree.root.value}")
    print(f"Отсортированные значения: {tree.get_sorted_values()}")
