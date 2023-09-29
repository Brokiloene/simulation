from entities.animals import Animal
from entities import Terrain, Grass
from utils import Bfs


class Herbivore(Animal):
    def __init__(self, coordinate, board_map, speed=2) -> None:
        super().__init__(coordinate, board_map, speed)

        self._sprite = ' H '


    def is_coordinate_free_to_move(self, coordinate):
        is_passable = super().is_coordinate_free_to_move(coordinate)

        if not is_passable or self.map.is_animal_exists_at(coordinate):
            return False
        return True


    def make_move(self):
        if self.map.is_terrain_exists_at(self.crd) and isinstance(self.map.get_object(Terrain, self.crd), Grass):
            self.map.del_object(Terrain, self.crd)
            # return
        
        path_to_target = Bfs.search(self, Terrain, Grass, self.map)
        
        if path_to_target:
            new_coordinate = self.find_optimal_coordinate_to_move(path_to_target)
            
            self.map.del_object(Animal, self.crd)
            self.map.move_object(Animal, new_coordinate, self)
            self.crd = new_coordinate
            return
        else:
            self.make_random_move()
