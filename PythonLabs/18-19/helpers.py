class Helpers:
    @staticmethod
    def is_power_of_two(number):
        """Returns True if given number is a power of two, False otherwise."""
        while number > 2:
            if number % 2 == 1:
                return False
            number = number // 2
        return number == 2

    @staticmethod
    def get_digits(number):
        """Returns generator for digits in the given number."""
        while number > 0:
            digit = number % 10
            number = number // 10
            yield digit

    @staticmethod
    def intersects(set1, set2):
        for i in set1:
            if i in set2:
                return True
        return False

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
