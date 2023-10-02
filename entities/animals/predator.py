from entities.animals.animal import Animal
from entities.animals.herbivore import Herbivore


class Predator(Animal):
    def __init__(self, coordinate, board_map, search_algorithm, speed=2) -> None:
        super().__init__(coordinate, board_map, search_algorithm, speed)
        
        self._sprite = ' P '
        self.target = Herbivore


    def is_coordinate_free_to_move(self, coordinate):
        is_passable = super().is_coordinate_free_to_move(coordinate)

        if not is_passable or \
            (self.map.is_animal_exists_at(coordinate) and isinstance(self.map.get_object(Animal, coordinate), Predator)):
        
            return False
            
        return True
