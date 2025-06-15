"""class Time with fields hours, minutes
method:
    Вычитание переменной типа Time (учесть, что возможен переход в
    предыдущие сутки). Результат должен быть типа Time.

Операции приведения типа:
    int – результатом является количество минут (время переводится в минуты);
    boolean – результатом является true, если часы и минуты не равны нулю,
        и false в противном случае.

Бинарные операции:
    < Time t – время переводится в минуты, результатом является true, если количество
        минут в левом операнде меньше, чем количество минут в правом операнде,
        и false – в противном случае.
    > Time t — время переводится в минуты, результатом является true, если количество
        минут в левом операнде больше, чем количество минут в правом операнде,
        и false – в противном случае."""


class Time:
    def __init__(self, hours, minutes):
        total_minutes = hours * 60 + minutes
        self.hours = (total_minutes // 60) % 24
        self.minutes = total_minutes % 60

    def __sub__(self, other):
        self_minutes = self.hours * 60 + self.minutes
        other_minutes = other.hours * 60 + other.minutes

        if self_minutes < other_minutes:
            diff_minutes = (24 * 60) + self_minutes - other_minutes
        else:
            diff_minutes = self_minutes - other_minutes

        return Time(0, diff_minutes)

    def __int__(self):
        return self.hours * 60 + self.minutes

    def __bool__(self):
        return self.hours != 0 or self.minutes != 0

    def __lt__(self, other):
        return int(self) < int(other)

    def __gt__(self, other):
        return int(self) > int(other)

    def __eq__(self, other):
        return int(self) == int(other)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"


def test_sub(time1, time2, res):
    diff = time1 - time2
    result = "OK" if res == diff else "FAIL"
    print(f"{result}: {time1} - {time2} = {diff}")


def test_conv_int(time, res):
    conv = int(time)
    result = "OK" if res == conv else "FAIL"
    print(f"{result}: {time} -(int)> {conv}")


def test_conv_bool(time, res):
    conv = bool(time)
    result = "OK" if res == conv else "FAIL"
    print(f"{result}: {time} -(bool)> {conv}")


def test_lt(time1, time2, res):
    diff = time1 < time2
    result = "OK" if res == diff else "FAIL"
    print(f"{result}: {time1} < {time2} = {diff}")


def test_gt(time1, time2, res):
    diff = time1 > time2
    result = "OK" if res == diff else "FAIL"
    print(f"{result}: {time1} > {time2} = {diff}")


if __name__ == "__main__":
    test_sub(Time(5, 30), Time(10, 31), Time(18, 59))

    test_conv_int(Time(1, 15), 75)

    test_conv_bool(Time(0, 0), False)
    test_conv_bool(Time(1, 0), True)
    test_conv_bool(Time(0, 1), True)

    low_time = Time(5, 10)
    high_time = Time(15, 20)
    test_lt(low_time, high_time, True)
    test_lt(high_time, low_time, False)
    test_lt(high_time, high_time, False)
    test_gt(low_time, high_time, False)
    test_gt(high_time, low_time, True)
    test_gt(high_time, high_time, False)
