from matrix import Matrix


class DistanceCalculator(Matrix):
    def __init__(self, filename):
        super().__init__()
        self.read_file(filename)
        self.distances = [25 for _ in range(self.size)]
        self.unvisited_nodes = [i for i in range(self.size)]

    def get_distances(self, source):
        self.distances[source] = 0

        while len(self.unvisited_nodes) > 0:
            current_node = self.__next_node()
            self.unvisited_nodes.remove(current_node)
            self.__fill_distances(current_node)

        return [i if not i == 25 else None for i in self.distances]

    def __next_node(self):
        next_node = -1
        min_dist = 25
        for node in self.unvisited_nodes:
            node_distance = self.distances[node]
            if node_distance < min_dist:
                min_dist = node_distance
                next_node = node
        return next_node

    def __fill_distances(self, current_node):
        next_distance = self.distances[current_node] + 1
        for node in self.unvisited_nodes:
            if self.get(current_node, node) > 0:
                self.distances[node] = min(self.distances[node], next_distance)
