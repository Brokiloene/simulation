import itertools

from entity import Entity
from bfs import BFS


class Creature(Entity):
    def __init__(self, x, y, board_size_x, board_size_y, speed, hp, graph) -> None:
        super().__init__(x, y, board_size_x, board_size_y)
        self.speed = speed
        self.hp
        self.graph = graph
# Сделать это абстрактным методом    
    def make_move(self, graph, dest):
        pass
    
    @property
    def possible_move_coordinates(self):
        """
        Лист кортежей всех координат, на которые может перейти данное существо
        """
        move_ranges = [x for x in range(-self.speed, self.speed + 1)]

        shifts = list(itertools.product(move_ranges, repeat=2))

        possible_moves = [(self.pos_x + x[0], self.pos_y + x[1]) for x in shifts]

        return filter(self.is_coordinate_valid, possible_moves)


class Herbivore(Creature):
    def make_move(self, dest):
        path_to_target = BFS(self.graph).search(self.coordinates, 'Grass')
        possible_moves = self.possible_move_coordinates

        if path_to_target is not None:
            for cord in path_to_target:
                pass


class Predator(Creature):
    pass