class Matrix:
    def __init__(self):
        self.size = 0
        self.arr = []
        pass

    def read_file(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        str_tokens = []
        for line in lines:
            if len(line) == 0 or line.startswith("//"):
                continue
            str_tokens = str_tokens + line.rsplit()
        try:
            tokens = [i for i in map(int, str_tokens)]
        except ValueError:
            return False

        if len(tokens) == 0:
            return False

        if not len(tokens) == tokens[0] ** 2 + 1:
            return False

        self.size = tokens[0]
        self.arr = tokens[1:]

        return True

    def get(self, x, y):
        return self.arr[self.__index(x, y)]

    def set(self, x, y, value):
        self.arr[self.__index(x, y)] = value

    def __str__(self):
        size = self.size
        for y in range(size):
            print(" ".join(map(str, self.arr[y * size : (y + 1) * size])))

    def __index(self, x, y):
        return y * self.size + x
