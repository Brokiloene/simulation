import random
import itertools

from entity import Entity
from bfs import BFS


class Animal(Entity):
    ANSI_BLINK = "\033[5m"

    MIN_HP = 1
    MAX_HP = 5

    def __init__(self, x, y, board_size_x, board_size_y, speed, terrain_graph, animal_graph) -> None:
        super().__init__(x, y, board_size_x, board_size_y)
        self.speed = speed
        self.hp = random.randint(self.MIN_HP, self.MAX_HP)
        self.terrain_graph = terrain_graph
        self.animal_graph = animal_graph
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
    
    def is_cord_free_to_move(self, cord):
        if isinstance(self, Herbivore) and cord in self.animal_graph:
            return False
        if (
            isinstance(self, Predator) and cord in self.animal_graph and
            isinstance(self.animal_graph[cord], Predator)
        ):
            return False
            
        return True

class Herbivore(Animal):
    ANSI_HERBIVORE = "\033[37m"

    def make_move(self, dest):
        path_to_target = BFS(self.terrain_graph).search(self.coordinates, 'Grass')
        possible_moves = self.possible_move_coordinates

        if path_to_target is not None:
            for cord in path_to_target:
                pass
    
    def __str__(self) -> str:
        return self.ANSI_BLINK + self.ANSI_HERBIVORE + " H " + self.ANSI_RESET

class Predator(Animal):
    ANSI_PREDATOR = "\033[38;05;196m"

    MIN_ATTACK = 1
    MAX_ATTACK = 3

    def __init__(self, x, y, board_size_x, board_size_y, speed, terrain_graph, animal_graph) -> None:
        super().__init__(x, y, board_size_x, board_size_y, speed, terrain_graph, animal_graph)
        self.attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK)

    def __str__(self) -> str:
        return self.ANSI_BLINK + self.ANSI_PREDATOR + " P " + self.ANSI_RESET