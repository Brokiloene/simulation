from entities.animals import Animal
from entities import Terrain, Grass


class Herbivore(Animal):
    def __init__(self, coordinate, board_map, search_algorithm, speed=2) -> None:
        super().__init__(coordinate, board_map, search_algorithm, speed)

        self._sprite = ' H '
        self.target = Grass


    def is_coordinate_free_to_move(self, coordinate):
        is_passable = super().is_coordinate_free_to_move(coordinate)

        if not is_passable or self.map.is_animal_exists_at(coordinate):
            return False
        return True
    

    def move_prepare(self):
        if self.map.is_terrain_exists_at(self.crd) and isinstance(self.map.get_object(Terrain, self.crd), Grass):
            self.map.del_object(Terrain, self.crd)

        return super().move_prepare()
