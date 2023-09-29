from entities.animals.animal import Animal
from entities.animals.herbivore import Herbivore

from utils import Bfs


class Predator(Animal):
    def __init__(self, coordinate, board_map, speed=2) -> None:
        super().__init__(coordinate, board_map, speed)
        
        self._sprite = ' P '

    def is_coordinate_free_to_move(self, coordinate):
        is_passable = super().is_coordinate_free_to_move(coordinate)

        if not is_passable or \
            (self.map.is_animal_exists_at(coordinate) and isinstance(self.map.get_object(Animal, coordinate), Predator)):
        
            return False
            
        return True
    
    
    def make_move(self):
        path_to_target = Bfs.search(self, Animal, Herbivore, self.map)

        if path_to_target:
            new_coordinate = self.find_optimal_coordinate_to_move(path_to_target)
            
            self.map.del_object(Animal, self.crd)
            self.map.move_object(Animal, new_coordinate, self)
            self.crd = new_coordinate
            return
        else:
            self.make_random_move()
