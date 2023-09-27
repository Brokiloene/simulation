import random

from entities.entity import Entity



class Terrain(Entity):
    pass

class Grass(Terrain):
    def __init__(self, coordinates, board_size) -> None:
        super().__init__(coordinates, board_size)
        self._sprite = random.choice([' ` ', ' " ', " ' ", ' , '])

class EmptyField(Terrain):
    def __str__(self) -> str:
        return '   '

class Rock(Terrain):
    def __init__(self, coordinates, board_size) -> None:
        super().__init__(coordinates, board_size)
        self._sprite = random.choice([' ☗ ', ' ⭓ '])
        self._is_passable = False


class Tree(Terrain):
    def __init__(self, coordinates, board_size) -> None:
        super().__init__(coordinates, board_size)
        self._sprite = random.choice([' ║ ', ' │ '])
