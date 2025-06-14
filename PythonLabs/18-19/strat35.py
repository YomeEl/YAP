"""Strat35. На доске написано число 2. Двое играют в игру, делая ходы по очереди: каждый из
игроков своим ходом может написать на доске любую степень двойки (то есть число вида 2k ,
k >1). Игрок, после хода которого на доске появятся две одинаковые цифры, проигрывает.
"""

from enum import IntEnum
from random import randint

from helpers import Helpers


class TwosPowerGame:
    """The twos power game logic"""

    def __init__(self):
        self.used_digits = [2]
        self.used_numbers = [2]
        self.is_first_player = True

    def find_digit(self, digit):
        """Returns True if given digit is present in used_digits, False otherwise."""
        return self.used_digits.count(digit) > 0

    def use_number(self, number):
        """Returns True if every digit in the given number is not present in used_digits
        and appends these digits to used_numbers.
        If any of the digits are already present, returns False."""
        for digit in Helpers.get_digits(number):
            if self.find_digit(digit):
                return False
            self.used_digits.append(digit)
        self.used_numbers.append(number)
        return True

    def input_power_of_two(self):
        """Repeatedly asks user to input a power of two and returns this number."""
        promt = "Введите число: "
        error_message = "Это не степень двойки!"
        return Helpers.input_with_condition(
            promt, error_message, int, Helpers.is_power_of_two
        )

    def make_move(self):
        """Plays one move of the game and returns True if winner was not determined.
        Otherwise returns False."""
        print(f"Ход {"первого" if self.is_first_player else "второго"} игрока")
        print("Числа на доске: " + " ".join(map(str, self.used_numbers)))
        number = self.input_power_of_two()
        self.is_first_player = not self.is_first_player
        return self.use_number(number)

    def print_result(self):
        print(f"{"Второй" if game.is_first_player else "Первый"} игрок победил!")


class BotDiffuculty(IntEnum):
    EASY = 3
    MEDIUM = 4
    HARD = 5


class TwosPowerGameSingle(TwosPowerGame):
    def __init__(self, is_player_first, difficulty):
        TwosPowerGame.__init__(self)
        self.is_player_first = is_player_first
        self.difficulty = difficulty

    def select_number(self):
        number = 0
        for _ in range(int(self.difficulty)):
            number = 2 ** randint(1, 31)
            if not Helpers.intersects(Helpers.get_digits(number), self.used_digits):
                return number
        return number

    def make_move(self):
        """Plays one move of the game and returns True if winner was not determined.
        Otherwise returns False."""

        print("Числа на доске: " + " ".join(map(str, self.used_numbers)))
        number = 0
        if self.is_first_player == self.is_player_first:
            print("Ваш ход")
            number = self.input_power_of_two()
        else:
            print("Ход бота")
            number = self.select_number()
            print(f"Бот пишет {number}")

        self.is_first_player = not self.is_first_player
        return self.use_number(number)

    def print_result(self):
        if self.is_first_player == self.is_player_first:
            print("Вы победили!")
        else:
            print("Вы проиграли!")


if __name__ == "__main__":
    player_variants = [("Один", True), ("Два", False)]
    difficulty_variants = [
        ("Лёгкий", BotDiffuculty.EASY),
        ("Средний", BotDiffuculty.MEDIUM),
        ("Сложный", BotDiffuculty.HARD),
    ]
    first_move_variants = [("Игрок", True), ("Бот", False)]

    is_single = Helpers.input_select("Выберите количество игроков:", player_variants)
    difficulty = BotDiffuculty.EASY
    if is_single:
        difficulty = Helpers.input_select(
            "Выберите уровень сложности:", difficulty_variants
        )
        is_player_first = Helpers.input_select("Кто ходит первым?", first_move_variants)

    game = (
        TwosPowerGameSingle(is_player_first, difficulty)
        if is_single
        else TwosPowerGame()
    )
    while game.make_move():
        continue
    game.print_result()
