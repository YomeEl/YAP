"""Strat29. Клетчатая доска 9 × 9 вся заполнена фишками. Петя и Вася играют в следующую игру:
за один ход можно выбрать горизонталь или вертикаль, на которой ещё остались фишки, и
снять оттуда все оставшиеся фишки. Выигрывает игрок, после хода которого доска опустеет.
"""

from helpers import Helpers


class Board:
    def __init__(self, size):
        self.size = size
        self.arr = [True for _ in range(size * size)]

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

    def copy(self):
        board = Board(self.size)
        board.arr = self.arr[:]
        return board

    def count_not_empty_rows(self):
        return self.__count_not_empty(self.count_row)

    def count_not_empty_columns(self):
        return self.__count_not_empty(self.count_column)

    def __count_not_empty(self, counter):
        count = 0
        for i in range(self.size):
            if counter(i) > 0:
                count = count + 1
        return count

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


class BoardGame:
    def __init__(self):
        self.board = Board(9)
        self.is_first_player = True

    def make_move(self):
        print("Текущее состояние доски:")
        print(self.board)
        print(f"Ход {"первого" if self.is_first_player else "второго"} игрока")
        dir = self._read_direction()
        index = self._read_index(dir)
        if dir == "r":
            self.board.remove_row(index)
        else:
            self.board.remove_column(index)
        self.is_first_player = not self.is_first_player
        return not self.board.is_empty()

    def print_result(self):
        print(f"{"Второй" if game.is_first_player else "Первый"} игрок победил!")

    def _read_direction(self):
        while True:
            dir = input(
                "Введите r, чтобы выбрать строку или c, чтобы выбрать столбец: "
            )
            if dir in ["r", "c"]:
                return dir
            print("Не удалось распознать направление!")

    def _read_index(self, direction):
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


class BoardGameSingle(BoardGame):
    def __init__(self, is_player_first):
        BoardGame.__init__(self)
        self.is_player_first = is_player_first

    def __is_board_winnable(self, board: Board):
        if board.is_empty():
            return True
        if board.count_not_empty_rows() % 2 == 0:
            return True
        if board.count_not_empty_columns() % 2 == 0:
            return True
        return False

    def __is_board_losable(self, board: Board):
        if board.count_not_empty_rows() == 1:
            return True
        if board.count_not_empty_columns() == 1:
            return True

    def __analyze(self, get_board):
        last_non_losable_candidate = None
        last_candidate = None
        for i in range(self.board.size):
            copy = get_board(i)
            if copy is None:
                continue
            last_candidate = i
            if self.__is_board_winnable(copy):
                return (last_candidate, last_candidate)
            if not self.__is_board_losable(copy):
                last_non_losable_candidate = last_candidate
        return (last_candidate, last_non_losable_candidate)

    def __find_move(self):
        def row_getter(i):
            if self.board.count_row(i) == 0:
                return None
            copy = self.board.copy()
            copy.remove_row(i)
            return copy

        def col_getter(i):
            if self.board.count_column(i) == 0:
                return None
            copy = self.board.copy()
            copy.remove_column(i)
            return copy

        row_result = self.__analyze(row_getter)
        col_result = self.__analyze(col_getter)

        if not row_result[1] is None:
            return ("r", row_result[1])
        if not col_result[1] is None:
            return ("c", col_result[1])
        if not row_result[0] is None:
            return ("r", row_result[0])
        return ("c", row_result[0])

    def make_move(self):
        print("Текущее состояние доски:")
        print(self.board)
        if self.is_first_player == self.is_player_first:
            print("Ваш ход")
            dir = self._read_direction()
            index = self._read_index(dir)
        else:
            print("Ход бота")
            dir, index = self.__find_move()
            print(
                f"Бот снимает фишки из {"строки" if dir == "r" else "столбца"} {index + 1}"
            )

        if dir == "r":
            self.board.remove_row(index)
        else:
            self.board.remove_column(index)
        self.is_first_player = not self.is_first_player
        return not self.board.is_empty()

    def print_result(self):
        if self.is_first_player == self.is_player_first:
            print("Вы проиграли!")
        else:
            print("Вы победили!")


if __name__ == "__main__":
    player_variants = [("Один", True), ("Два", False)]
    first_move_variants = [("Игрок", True), ("Бот", False)]

    is_single = Helpers.input_select("Выберите количество игроков:", player_variants)
    if is_single:
        is_player_first = Helpers.input_select("Кто ходит первым?", first_move_variants)

    game = BoardGameSingle(is_player_first) if is_single else BoardGame()
    while game.make_move():
        continue
    game.print_result()
