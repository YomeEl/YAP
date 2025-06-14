from matrix import Matrix


class VertexDegreesCalculator(Matrix):
    def __init__(self, filename):
        super().__init__()
        self.read_file(filename)

    def get_degrees(self):
        return [self.__count_row(i) for i in range(self.size)]

    def __count_row(self, index):
        count = 0
        for i in range(self.size):
            if self.get(i, index) > 0:
                count = count + 1
                if i == index:
                    count = count + 1
        return count


if __name__ == "__main__":
    filename = "graph_test.txt"
    vdc = VertexDegreesCalculator(filename)
    print(vdc.get_degrees())
