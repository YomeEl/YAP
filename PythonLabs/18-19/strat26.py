"""Strat26. В тетради написаны буквы русского и английского алфавитов, всего вместе 59 букв.
Артём и Надя по очереди вычеркивают буквы, причём за раз можно вычеркнуть или 1, или 2,
или 4, или 5 букв. Тот, кто не сможет сделать ход, проигрывает."""

from enum import Enum
from random import randint

from helpers import Helpers


class LettersGame:
    """Letters game logic."""

    class InputProcessingResult(Enum):
        """Input processing result enum."""

        OK = 1
        INVALID_LETTER = 2
        NON_EXISTING_LETTER = 3
        INVALID_COUNT = 4
        NOT_UNIQUE_LETTER = 5

    def __init__(self):
        self.is_first_player = True
        self.letters = []
        for i in range(ord("а"), ord("е") + 1):
            self.letters.append(chr(i))
        self.letters.append("ё")
        for i in range(ord("ж"), ord("я") + 1):
            self.letters.append(chr(i))
        for i in range(ord("a"), ord("z") + 1):
            self.letters.append(chr(i))

    def make_move(self):
        """Prints whose move it is, requests letters to remove and removes them.
        Returns true if next move is possible and False otherwise."""
        print(f"Ход {"первого" if self.is_first_player else "второго"} игрока")
        print("Буквы на доске:")
        self.__print_letters()
        letters = self.__request_letters()
        self.__remove_letters(letters)
        self.is_first_player = not self.is_first_player
        return len(self.letters) not in [0, 3]

    def print_result(self):
        if len(self.letters) > 0:
            print("Буквы на доске: ")
            self.__print_letters()

        print(f"{"Первый" if self.is_first_player else "Второй"} игрок победил!")

    def __is_valid_letter(self, letter):
        """returns True if provided letter is valid, otherwise False"""
        is_cyrillic = ord(letter) in range(ord("а"), ord("я") + 1) or letter == "ё"
        is_latin = ord(letter) in range(ord("a"), ord("z") + 1)
        return is_cyrillic or is_latin

    def __print_letters(self):
        """Prints unused letters to stdout."""
        print(" ".join(self.letters))

    def __process_input(self, input_string):
        """Checks input_string and returns tuple of InputProcessingResult enum and result.
        Result is list of letters if all checks passed, problematic letter if letter is invalid
        or not present and empty if count of letters is invalid."""
        letters = input_string.split(" ")
        valid_counts = [1, 2, 4, 5]
        if not len(letters) in valid_counts:
            return self.InputProcessingResult.INVALID_COUNT, ""

        for letter in letters:
            if not len(letter) == 1 or not self.__is_valid_letter(letter):
                return self.InputProcessingResult.INVALID_LETTER, letter
            if not letter in self.letters:
                return self.InputProcessingResult.NON_EXISTING_LETTER, letter
            if letters.count(letter) > 1:
                return self.InputProcessingResult.NOT_UNIQUE_LETTER, letter

        return self.InputProcessingResult.OK, letters

    def __print_error(self, error, result):
        """Prints details of the given error using result."""
        match error:
            case self.InputProcessingResult.INVALID_COUNT:
                print("Введено неверное количество букв!")
            case self.InputProcessingResult.INVALID_LETTER:
                print(f"Буквы {result} не существует!")
            case self.InputProcessingResult.NON_EXISTING_LETTER:
                print(f"Буквы {result} нет на доске!")
            case self.InputProcessingResult.NOT_UNIQUE_LETTER:
                print(f"Буква {result} введена более одного раза!")
            case _:
                print("OK")

    def __request_letters(self):
        """Repeatedly asks user to input valid number of valid letters. Returns these letters."""
        while True:
            promt = (
                "Ведите через пробел одну, две, четыре "
                "или пять букв, которые хотите зачеркунть: "
            )
            error, letters = self.__process_input(input(promt))
            if error == self.InputProcessingResult.OK:
                return letters
            self.__print_error(error, letters)

    def __remove_letters(self, letters):
        """Removes letters from self.letters"""
        for letter in letters:
            self.letters.remove(letter)


class LettersGameSingle(LettersGame):
    def __init__(self, is_player_first):
        LettersGame.__init__(self)
        self.is_player_first = is_player_first

    def __select_count_to_remove(self):
        letters_count = len(self.letters)
        if letters_count == 3:
            return 2
        special_counts = [1, 2, 4, 5]
        if letters_count in special_counts:
            return letters_count

        if letters_count - 3 in special_counts:
            return letters_count - 3

        return special_counts[randint(0, 3)]

    def __select_letters_to_remove(self):
        count = self.__select_count_to_remove()
        return self.letters[:count]

    def make_move(self):
        """Prints whose move it is, requests letters to remove and removes them.
        Returns true if next move is possible and False otherwise."""

        print("Буквы на доске: ")
        self.__print_letters()

        letters = []
        if self.is_first_player == self.is_player_first:
            print("Ваш ход")
            letters = self.__request_letters()
        else:
            print("Ход бота")
            letters = self.__select_letters_to_remove()
            print(f"Бот вычёркивает {", ".join(letters)}")

        self.__remove_letters(letters)
        self.is_first_player = not self.is_first_player
        return len(self.letters) not in [0, 3]

    def print_result(self):
        if len(self.letters) > 0:
            print("Буквы на доске: ")
            self.__print_letters()

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

    game = LettersGameSingle(is_player_first) if is_single else LettersGame()
    while game.make_move():
        continue
    game.print_result()
