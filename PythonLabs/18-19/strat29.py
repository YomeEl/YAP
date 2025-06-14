"""Strat29. Клетчатая доска 9 × 9 вся заполнена фишками. Петя и Вася играют в следующую игру:
за один ход можно выбрать горизонталь или вертикаль, на которой ещё остались фишки, и
снять оттуда все оставшиеся фишки. Выигрывает игрок, после хода которого доска опустеет.
"""


class Board:
    def __init__(self, size):
        self.size = size
        self.arr = [True for _ in range(size * size)]

    def __str__(self):
        header = "  " + (
            "\u0332 ".join(["\u0332" + str(i + 1) for i in range(self.size)])
        )
        lines = [
            "|".join([str(i + 1)] + self.__get_str_line(i)) for i in range(self.size)
        ]
        return "\n".join([header] + lines)

    def __index(self, x, y):
        return y * self.size + x

    def __get(self, x, y):
        return self.arr[self.__index(x, y)]

    def __set(self, x, y, value):
        self.arr[self.__index(x, y)] = value

    def __get_str_line(self, index):
        return [
            "\u0332" + ("o" if self.__get(i, index) else " ") for i in range(self.size)
        ]

    def count_row(self, index):
        if index >= self.size:
            return -1
        count = 0
        for i in range(self.size):
            count = count + (1 if self.__get(i, index) else 0)
        return count

    def count_column(self, index):
        if index >= self.size:
            return -1
        count = 0
        for i in range(self.size):
            count = count + (1 if self.__get(index, i) else 0)
        return count

    def remove_row(self, index):
        if index >= self.size:
            return -1
        for i in range(self.size):
            self.__set(i, index, False)

    def remove_column(self, index):
        if index >= self.size:
            return -1
        for i in range(self.size):
            self.__set(index, i, False)

    def is_empty(self):
        for i in range(self.size * self.size):
            if self.arr[i]:
                return False
        return True


class BoardGame:
    def __init__(self):
        self.board = Board(9)
        self.is_first_player = True

    def __read_direction(self):
        while True:
            dir = input(
                "Введите r, чтобы выбрать строку или c, чтобы выбрать столбец: "
            )
            if dir in ["r", "c"]:
                return dir
            print("Не удалось распознать направление!")

    def __read_index(self, direction):
        while True:
            is_row = direction == "r"
            promt = f"Введите номер {"строки" if is_row else "стоблца"}: "
            index = 0
            try:
                index = int(input(promt)) - 1
            except ValueError:
                print("Не удалось распознать число!")
                continue

            if index not in range(self.board.size):
                print("Неверно указан индекс!")
                continue

            count_fnc = self.board.count_row if is_row else self.board.count_column
            if count_fnc(index) == 0:
                empty_row_str = "Выбранная строка пуста!"
                empty_column_str = "Выбранный столбец пуст!"
                print(empty_row_str if is_row else empty_column_str)
                continue

            return index

    def make_move(self):
        print("Текущее состояние доски:")
        print(self.board)
        print(f"Ход {"первого" if self.is_first_player else "второго"} игрока")
        dir = self.__read_direction()
        index = self.__read_index(dir)
        if dir == "r":
            self.board.remove_row(index)
        else:
            self.board.remove_column(index)
        self.is_first_player = not self.is_first_player
        return not self.board.is_empty()


if __name__ == "__main__":
    game = BoardGame()
    while game.make_move():
        continue

    print(f"{"Второй" if game.is_first_player else "Первый"} игрок победил!")
