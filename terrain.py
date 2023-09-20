import random

from entity import Entity


class Terrain(Entity):
    def __init__(self, x, y, board_size_x, board_size_y) -> None:
        super().__init__(x, y, board_size_x, board_size_y)

    @property
    def name(self):
        return type(self).__name__


class Grass(Terrain):
    def __str__(self) -> str:
        return random.choice(['`', '"', "'", ','])


class Rock(Terrain):
    def __str__(self) -> str:
        return random.choice(['•', '.', '·'])


class Tree(Terrain):
    def __str__(self) -> str:
        return random.choice(['║', '│'])
