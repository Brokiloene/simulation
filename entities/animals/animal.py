import random
import itertools
import abc

from utils import Coordinate
from entities import Entity, Terrain, Rock



class Animal(Entity):
    def __init__(self, coordinate, board_map, speed) -> None:
        super().__init__(coordinate)
        self.map = board_map
        self.speed = speed


    @abc.abstractmethod
    def make_move(self):
        pass


    def is_coordinate_free_to_move(self, coordinate):
        if self.map.is_terrain_exists_at(coordinate) and isinstance(self.map.get_object(Terrain, coordinate), Rock):
            return False

        return True

    
    def make_random_move(self):
        # если нет цели или до неё не дойти, сделать случайный ход
        possible_moves = list(filter(self.is_coordinate_free_to_move, self.map.get_neighbor_coordinates_of(self.crd)))
        
        if not possible_moves:
            return
        
        new_coordinate = random.choice(possible_moves)

        self.map.del_object(Animal, self.crd)
        self.map.move_object(Animal, new_coordinate, self)
        self.crd = new_coordinate


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

        return list(filter(self.map.is_given_coordinate_valid , possible_moves))
