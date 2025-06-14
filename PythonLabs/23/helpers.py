from bin_tree import parse_bin_tree


class Helpers:
    @staticmethod
    def input_with_condition(promt, error_message, converter, condition):
        """Repeatedly asks user to input something, while condition is not satisfied."""
        while True:
            try:
                number = converter(input(promt))
            except ValueError:
                print("Неверный ввод!")
                continue
            except KeyboardInterrupt:
                exit(0)
            if condition(number):
                return number
            print(error_message)

    @staticmethod
    def input_select(promt, variants):
        print(promt)
        for i in range(len(variants)):
            print(f"\t{str(i + 1)}. {variants[i][0]}")

        condition = lambda i: (i - 1) in range(len(variants))
        index = Helpers.input_with_condition(
            "Введите номер: ", "Неверный номер!", int, condition
        )
        return variants[index - 1][1]

    @staticmethod
    def read_tree():
        while True:
            try:
                print("<Цифра> := 0|1|2|3|4|5|6|7|8|9")
                print("<Число> := [-]<Цифра>[<Число>]")
                print("<Дерево> := <Число>[([<Дерево>],[<Дерево>])]")
                tree_string = input("Введите <Дерево>: ")
                return parse_bin_tree(tree_string)
            except ValueError:
                print("Неверный формат входных данных")
