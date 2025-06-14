from distance_calculator import DistanceCalculator


class GreaterOrEqualDistanceFinder(DistanceCalculator):
    def __init__(self, filename):
        super().__init__(filename)

    def get_nodes_with_exact_distance(self, source, distance):
        result = []
        for i, current_distance in enumerate(self.get_distances(source)):
            if current_distance >= distance:
                result.append(i)
        return result


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


if __name__ == "__main__":
    filename = "graph_test.txt"
    try:
        worker = GreaterOrEqualDistanceFinder(filename)
    except:
        print("Ошибка при чтении файла!")
        exit(1)

    k_promt = "Введите начальный город K: "
    l_promt = "Введите минимальное количество пересадок L: "
    error_message = "Неверный ввод!"

    k_condition = lambda k: k > 0 and k <= worker.size
    l_condition = lambda l: l >= 0

    k = input_with_condition(k_promt, error_message, int, k_condition)
    l = input_with_condition(l_promt, error_message, int, l_condition)

    result = worker.get_nodes_with_exact_distance(k - 1, l)
    print("Результат: ", end="")
    if len(result) == 0:
        print(-1)
    else:
        print(" ".join(map(lambda i: str(i + 1), result)))
