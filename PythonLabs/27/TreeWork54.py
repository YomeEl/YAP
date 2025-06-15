"""TreeWork54. Дан текстовый файл, в первой строке которого записана последовательность
неповторяющихся целых чисел. Числа разделены пробелами. Необходимо построить из этих
чисел дерево поиска и вывести корень дерева P1"""

from bin_tree import BinTree


def read_file(filename) -> list[int]:
    file = open(filename)
    line = file.readline()
    file.close()
    return [int(token) for token in line.rsplit()]


if __name__ == "__main__":
    try:
        numbers = read_file("test54.txt")
    except:
        print("Ошибка при чтении файла!")
        exit()

    tree = BinTree()
    for number in numbers:
        tree.insert(number)

    print(f"Дерево поиска: {tree}")
    print(f"Корень дерева: {tree.root.value}")
