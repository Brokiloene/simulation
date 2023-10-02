import itertools

from utils import Coordinate
from entities import Terrain, Rock, Tree, Grass, Animal, Herbivore, Predator


class SimulationMap:
    def __init__(self, board_size_row, board_size_col, search_algorithm) -> None:
        self.bd_area = board_size_col * board_size_row

        self.bd_size_row = board_size_row
        self.bd_size_col = board_size_col
        self.bd_max_crd = Coordinate(self.bd_size_row, self.bd_size_col)
        self.bd_area = self.bd_size_row * self.bd_size_col

        self.search_algo = search_algorithm

        # животные могут ходить "поверх" местности, поэтому отдельный словарь
        self.terrain_graph = {}
        self.animal_graph = {}

        self.terrain_objects = (Rock, Tree, Grass)
        self.animal_objects  = (Herbivore, Predator)

        self.passable_terrain = (Tree, Grass, type(None))

    @property
    def bd_size_row(self):
        return self._bd_size_row


    @bd_size_row.setter
    def bd_size_row(self, board_size_row):
        self._bd_size_row = board_size_row


    @property
    def bd_size_col(self):
        return self._bd_size_col
    

    @bd_size_col.setter
    def bd_size_col(self, board_size_col):
        self._bd_size_col = board_size_col


    @property
    def search_algo(self):
        return self._search_algo


    @search_algo.setter
    def search_algo(self, search_algorithm):
        if search_algorithm not in ("BFS", "A*"):
            raise Exception("Unknown search algorithm")
        self._search_algo = search_algorithm


    def instantiate_object(self, graph_type, cls, coordinate):
        match graph_type.__name__:
            case Terrain.__name__:
                self.terrain_graph[coordinate] = cls(coordinate)
            case Animal.__name__:
                self.animal_graph[coordinate] = cls(coordinate, self, self.search_algo)
            case _:
                raise ValueError("Wrong graph_type in SimulationMap.set_object()")


    def init_map_manual(self):
        # self.instantiate_object(Animal, Predator, Coordinate(0, 0))
        # self.instantiate_object(Animal, Herbivore, Coordinate(1, 0))
        pass


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


    def is_coordinate_exists_at(self, coordinate):
        return self.is_animal_exists_at(coordinate) or self.is_terrain_exists_at(coordinate)


    def is_given_coordinate_valid(self, coordinate):
        if Coordinate(0, 0) <= coordinate < self.bd_max_crd and \
            (not coordinate in self.terrain_graph or isinstance(self.terrain_graph[coordinate], self.passable_terrain) ):
            return True

        return False


    def get_neighbor_coordinates_of(self, coordinate):
        neighbor_coordinates = []

        for shift in list(itertools.product(range(-1, 2), range(-1, 2))):
            if shift == (0, 0):
                continue

            cur_crd = Coordinate(coordinate.row + shift[0], coordinate.col + shift[1])
            if self.is_given_coordinate_valid(cur_crd):
               neighbor_coordinates.append(cur_crd)

        return neighbor_coordinates


    def count_instances_of(self, cls):
        all_objects = list(self.terrain_graph.values()) + list(self.animal_graph.values())
        found = [x for x in all_objects if isinstance(x, cls)]
        return len(found)


    def find_neares_object_crd(self, start_crd, target_cls):
        def calc_distance(start_crd, target_crd):
            return int(((start_crd.row - target_crd.row) ** 2 + (start_crd.col - target_crd.col) ** 2) ** 0.5)


        if target_cls in self.terrain_objects:
            all_instances = [obj for obj in self.terrain_graph.values() if isinstance(obj, target_cls)]
        elif target_cls in self.animal_objects:
            all_instances = [obj for obj in self.animal_graph.values() if isinstance(obj, target_cls)]
        else:
            raise TypeError("Wrong target_cls in Simulation.find_neares_object_crd")
        
        res_crd = None
        min_distance = None
        for obj in all_instances:
            if res_crd is None or min_distance > calc_distance(start_crd, obj.crd):
                res_crd = obj.crd
                min_distance = calc_distance(start_crd, obj.crd)
        
        return res_crd


    @property
    def all_possible_coordinates(self):
        """
        Лист кортежей всех координат всех клеток поля
        """
        return [ Coordinate(*x) for x in itertools.product([*range(self.bd_size_row)], [*range(self.bd_size_col)]) ]
