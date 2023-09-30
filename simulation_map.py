import itertools
import random

from utils import Coordinate
from entities import Terrain, Rock, Tree, Grass, Animal, Herbivore, Predator



class SimulationMap:
    def __init__(self, board_size_row, board_size_col) -> None:
        self.bd_size_row = board_size_row
        self.bd_size_col = board_size_col
        self.bd_max_crd = Coordinate(self.bd_size_row, self.bd_size_col)
        self.bd_area = self.bd_size_row * self.bd_size_col

        self.terrain_graph = {}
        self.animal_graph = {}

        self.terrain_objects = (Rock, Tree, Grass)
        self.animal_objects  = (Herbivore, Predator)

        self.passable_terrain = (Tree, Grass, None)
    

    def instantiate_object(self, graph_type, cls, coordinate):
        match graph_type.__name__:
            case Terrain.__name__:
                self.terrain_graph[coordinate] = cls(coordinate)
            case Animal.__name__:
                self.animal_graph[coordinate] = cls(coordinate, self)
            case _:
                raise ValueError("Wrong graph_type in SimulationMap.set_object()")


    def init_map_manual(self):
        self.instantiate_object(Animal, Predator, Coordinate(0, 0))

        self.instantiate_object(Animal, Herbivore, Coordinate(1, 0))
        self.instantiate_object(Animal, Herbivore, Coordinate(0, 1))
        self.instantiate_object(Animal, Herbivore, Coordinate(1, 1))

        self.instantiate_object(Terrain, Rock, Coordinate(2, 0))
        self.instantiate_object(Terrain, Rock, Coordinate(2, 1))
        self.instantiate_object(Terrain, Rock, Coordinate(0, 2))

        self.instantiate_object(Terrain, Tree, Coordinate(2, 2))
        self.instantiate_object(Terrain, Tree, Coordinate(1, 2))

        self.instantiate_object(Terrain, Grass, Coordinate(0, 3))
        self.instantiate_object(Terrain, Grass, Coordinate(1, 3))
        self.instantiate_object(Terrain, Grass, Coordinate(2, 3))
        self.instantiate_object(Terrain, Grass, Coordinate(3, 3))
        self.instantiate_object(Terrain, Grass, Coordinate(3, 2))
        self.instantiate_object(Terrain, Grass, Coordinate(3, 1))
        self.instantiate_object(Terrain, Grass, Coordinate(3, 0))

        # self.instantiate_object(Animal, Herbivore, Coordinate(0, 3))

        # self.instantiate_object(Terrain, Grass, Coordinate(0, 0))

        # self.instantiate_object(Terrain, Rock, Coordinate(0, 1))
        # self.instantiate_object(Terrain, Rock, Coordinate(0, 2))
        # self.instantiate_object(Terrain, Rock, Coordinate(1, 0))
        # self.instantiate_object(Terrain, Rock, Coordinate(1, 2))
        # self.instantiate_object(Terrain, Rock, Coordinate(2, 1))
        # self.instantiate_object(Terrain, Rock, Coordinate(2, 2))
        # self.instantiate_object(Terrain, Rock, Coordinate(1, 1))
        

    def init_map_random(self):
        all_crd = self.all_possible_coordinates
        
        # животных не должно быть слишком много
        crd_for_animals = random.choices(all_crd, k=int(self.bd_area ** 0.5))
        
        crd_for_terrain = random.choices(all_crd, k=random.randint(self.bd_area // 2, self.bd_area))
        
        for crd in crd_for_animals:
            animals_to_set = random.choices(self.animal_objects, [5, 1], k=len(crd_for_animals))
            for animal_type in animals_to_set:
                self.instantiate_object(Animal, animal_type, crd)

        for crd in crd_for_terrain:
            terrain_type = random.choice(self.terrain_objects)
            self.instantiate_object(Terrain, terrain_type, crd)
            

    def get_object(self, graph_type, coordinate):
        match graph_type.__name__:
            case Terrain.__name__:
                return self.terrain_graph[coordinate]
            case Animal.__name__:
                return self.animal_graph[coordinate]
            case _:
                raise ValueError("Wrong graph_type in SimulationMap.get_object()")


    @property
    def get_animals(self):
        return list(self.animal_graph.values())
    

    @property
    def get_terrains(self):
        return list(self.terrain_graph.values())


    def del_object(self, graph_type, coordinate):
        match graph_type.__name__:
            case Terrain.__name__:
                del self.terrain_graph[coordinate]
            case Animal.__name__:
                del self.animal_graph[coordinate]
            case _:
                raise ValueError("Wrong graph_type in SimulationMap.del_object()")
    

    def move_object(self, graph_type, coordinate, object_to_move):
        match graph_type.__name__:
            case Terrain.__name__:
                self.terrain_graph[coordinate] = object_to_move
            case Animal.__name__:
                self.animal_graph[coordinate] = object_to_move
            case _:
                raise ValueError("Wrong graph_type in SimulationMap.move_object()")


    def is_object_exists(self, obj):
        return obj in self.animal_graph.values() or obj in self.terrain_graph.values()


    def is_animal_exists_at(self, coordinate):
        return coordinate in self.animal_graph


    def is_terrain_exists_at(self, coordinate):
        return coordinate in self.terrain_graph


    def is_given_coordinate_valid(self, coordinate):
        return Coordinate(0, 0) <= coordinate < self.bd_max_crd


    def get_neighbor_coordinates_of(self, coordinate):
        """
        Вернёт список объектов Coordinate -- координаты клеток-соседей self
        """
        neighbor_coordinates = []

        for shift in list(itertools.product(range(-1, 2), range(-1, 2))):
            if shift == (0, 0):
                continue

            cur_crd = Coordinate(coordinate.row + shift[0], coordinate.col + shift[1])
            if self.is_given_coordinate_valid(cur_crd):   
               neighbor_coordinates.append(cur_crd)

        return neighbor_coordinates
    

    @property
    def all_possible_coordinates(self):
        """
        Лист кортежей всех координат всех клеток поля
        """
        return [ Coordinate(*x) for x in itertools.product([*range(self.bd_size_row)], [*range(self.bd_size_col)]) ]