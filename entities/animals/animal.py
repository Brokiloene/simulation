import random
import itertools
import abc

from utils.coordinate import Coordinate
from utils.bfs import Bfs
from entities.entity import Entity
from entities.terrain import Rock



class Animal(Entity):
    def __init__(self, coordinate, board_size, terrain_graph, animal_graph, speed) -> None:
        self.crd = coordinate
        self.bd_size = board_size

        self.t_graph = terrain_graph
        self.a_graph = animal_graph

        self.speed = speed


    @abc.abstractmethod
    def make_move(self):
        pass


    def is_coordinate_free_to_move(self, coordinate):
        if coordinate in self.t_graph and isinstance(self.t_graph[coordinate], Rock):
            return False
        
        return True

    
    def make_random_move(self):
        # если нет цели или до неё не дойти, сделать случайный ход
        possible_moves = list(filter(self.is_coordinate_free_to_move, self.crd.neighbor_coordinates(self.bd_size)))
        if not possible_moves:
            return
        new_coordinates = random.choice(possible_moves)
        del self.a_graph[self.crd]
        self.a_graph[new_coordinates] = self
        self.crd = new_coordinates



    def find_optimal_coordinate_to_move(self, path_to_target):
        move_to_crd = path_to_target[0]
        possible_moves = self.possible_move_coordinates

        for ind in range(min(self.speed, len(path_to_target))):
            new_crd = path_to_target[ind]
            if new_crd in possible_moves and self.is_coordinate_free_to_move(new_crd):
                move_to_crd = new_crd
            else:
                return move_to_crd
            
        return move_to_crd
    

    @property
    def possible_move_coordinates(self):
        """
        Лист координат, на которые может перейти данное существо
        """
        move_ranges = [x for x in range(-self.speed, self.speed + 1)]

        shifts = list(itertools.product(move_ranges, repeat=2))

        possible_moves = [self.crd + Coordinate(*shift) for shift in shifts]

        return list(filter(lambda x: Coordinate(0, 0) <= x < self.bd_size, possible_moves))
    

    @property
    def coordinate_is_reachable_in_one_move(self, coordinate):
        """
        Животные могут пройти перепрыгнуть несколько клеток за один ход, но не через камни
        """



