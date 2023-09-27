import random
import itertools

from coordinates import Coordinates
from entity import Entity
from terrain import Grass, EmptyField
from bfs import BFS


class Animal(Entity):
    ANSI_BLINK = "\033[5m"

    MIN_HP = 1
    MAX_HP = 5

    def __init__(self, coordinates, board_size, speed, terrain_graph, animal_graph) -> None:
        super().__init__(coordinates, board_size)

        self.speed = speed
        self.terrain_graph = terrain_graph
        self.animal_graph = animal_graph

        self.hp = random.randint(self.MIN_HP, self.MAX_HP)
# Сделать это абстрактным методом    
    def make_move(self):
        pass
    
    @property
    def possible_move_coordinates(self):
        """
        Лист координат, на которые может перейти данное существо
        """
        move_ranges = [x for x in range(-self.speed, self.speed + 1)]

        shifts = list(itertools.product(move_ranges, repeat=2))

        possible_moves = [self.coordinates + Coordinates(*shift) for shift in shifts]

        return list(filter(lambda x: Coordinates(0, 0) <= x < self.board_size, possible_moves))
    
    def is_coordinates_free_to_move(self, cord):
        pass

class Herbivore(Animal):
    ANSI_HERBIVORE = "\033[37m"

    def is_coordinates_free_to_move(self, cord):
        if cord in self.animal_graph:
            return False
            
        return True

    def make_move(self):

        if self.coordinates in self.terrain_graph and isinstance(self.terrain_graph[self.coordinates], Grass):
            del self.terrain_graph[self.coordinates]
            self.terrain_graph[self.coordinates] = EmptyField(self.coordinates, self.board_size)
            return
        
        path_to_target = BFS(self.terrain_graph).search(self.coordinates, 'Grass', self.board_size)
        possible_moves = self.possible_move_coordinates

        if path_to_target is not None:
            for new_coordinates in path_to_target:
                if new_coordinates in possible_moves and self.is_coordinates_free_to_move(new_coordinates):
                    del self.animal_graph[self.coordinates]
                    self.animal_graph[new_coordinates] = self
                    self.coordinates = new_coordinates
                    
                    return
                    
        # если нет цели или до неё не дойти, сделать случайный ход
        possible_moves = list(filter(self.is_coordinates_free_to_move, possible_moves))
        if not possible_moves:
            return
        new_coordinates = random.choice(possible_moves)
        del self.animal_graph[self.coordinates]
        self.animal_graph[new_coordinates] = self
        self.coordinates = new_coordinates
    
    def __str__(self) -> str:
        return self.ANSI_BLINK + self.ANSI_HERBIVORE + " H " + self.ANSI_RESET

class Predator(Animal):
    ANSI_PREDATOR = "\033[38;05;196m"

    MIN_ATTACK = 1
    MAX_ATTACK = 3

    def __init__(self, coordinates, board_size, speed, terrain_graph, animal_graph) -> None:
        super().__init__(coordinates, board_size, speed, terrain_graph, animal_graph)
        self.attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK)

    def __str__(self) -> str:
        return self.ANSI_BLINK + self.ANSI_PREDATOR + " P " + self.ANSI_RESET

    def is_coordinates_free_to_move(self, cord):
        if cord in self.animal_graph and isinstance(self.animal_graph[cord], Predator):
            return False
            
        return True
    
    def make_move(self):
        path_to_target = BFS(self.animal_graph).search(self.coordinates, 'Herbivore', self.board_size)
        possible_moves = self.possible_move_coordinates

        if path_to_target is not None:
            for new_coordinates in path_to_target:
                if new_coordinates in possible_moves and self.is_coordinates_free_to_move(new_coordinates):
                    del self.animal_graph[self.coordinates]
                    self.animal_graph[new_coordinates] = self
                    self.coordinates = new_coordinates
                    
                    return
                    
        # если нет цели или до неё не дойти, сделать случайный ход
        possible_moves = list(filter(self.is_coordinates_free_to_move, possible_moves))
        if not possible_moves:
            return
        new_coordinates = random.choice(possible_moves)
        del self.animal_graph[self.coordinates]
        self.animal_graph[new_coordinates] = self
        self.coordinates = new_coordinates

# if __name__ == '__main__':
#     h = Herbivore(Coordinates(2, 2), Coordinates(5, 5), 2, {}, {})
#     print(*h.possible_move_coordinates)