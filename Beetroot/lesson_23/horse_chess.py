class Horse:

    def __init__(self, x: int = 0, y: int = 0):
        self.__x = x
        self.__y = y
        self.dist = 0
        self.visited_cells = [self.current_position]
        self.possible_steps = [(2, 1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (2, -1)]

    @property
    def current_position(self):
        return self.__x, self.__y

    @current_position.setter
    def current_position(self, new_position):
        self.__x = new_position[0]
        self.__y = new_position[1]


class Board:

    def __init__(self, size: int = 8):
        self.size = size

    def is_valid(self, position):
        return 1 <= position[0] <= self.size and 1 <= position[1] <= self.size

    def shortest_way(self, figure, destination):

        for step in figure.possible_steps:
            if figure.current_position == destination:
                return figure.dist, figure.visited_cells

            next_position = figure.current_position[0] + step[0], figure.current_position[1] + step[1]

            if self.is_valid(next_position) and self.is_valid(destination) and next_position not in figure.visited_cells:
                # print(figure.current_position)
                figure.current_position = next_position
                figure.dist += 1
                # print('next', next_position)
                figure.visited_cells.append(next_position)
                self.shortest_way(figure, destination)


if __name__ == '__main__':
    horse = Horse(1, 1)
    board = Board()
    print(board.shortest_way(horse, destination=(8, 8)))
