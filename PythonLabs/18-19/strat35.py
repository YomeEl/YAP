"""Strat35. На доске написано число 2. Двое играют в игру, делая ходы по очереди: каждый из
игроков своим ходом может написать на доске любую степень двойки (то есть число вида 2k ,
k >1). Игрок, после хода которого на доске появятся две одинаковые цифры, проигрывает.
"""


class TwosPowerGame:
    """The twos power game logic"""

    def __init__(self):
        self.used_digits = [2]
        self.is_first_player = True

    def find_digit(self, digit):
        """Returns True if given digit is present in used_digits, False otherwise."""
        return self.used_digits.count(digit) > 0

    def is_power_of_two(self, number):
        """Returns True if given number is a power of two, False otherwise."""
        while number > 2:
            number = number // 2
        return number == 2

    def get_digits(self, number):
        """Returns generator for digits in the given number."""
        while number > 0:
            digit = number % 10
            number = number // 10
            yield digit

    def use_number(self, number):
        """Returns True if every digit in the given number is not present in used_digits
        and appends these digits to used_numbers.
        If any of the digits are already present, returns False."""
        for digit in self.get_digits(number):
            if self.find_digit(digit):
                return False
            self.used_digits.append(digit)
        return True

    def input_power_of_two(self):
        """Repeatedly asks user to input a power of two and returns this number."""
        while True:
            print("Введите число: ", end="")
            number = int(input())
            if self.is_power_of_two(number):
                return number
            print("Это не степень двойки!")

    def make_move(self):
        """Plays one move of the game and returns True if winner was not determined.
        Otherwise returns False."""
        print(f"Ход {"первого" if self.is_first_player else "второго"} игрока")
        number = self.input_power_of_two()
        if not self.use_number(number):
            return False
        self.is_first_player = not self.is_first_player
        return True


if __name__ == "__main__":
    game = TwosPowerGame()
    while game.make_move():
        continue

    print(f"{"Второй" if game.is_first_player else "Первый"} игрок победил!")
