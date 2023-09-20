import random

from entity import Entity


class Terrain(Entity):
    def __init__(self, x, y, board_size_x, board_size_y) -> None:
        super().__init__(x, y, board_size_x, board_size_y)

    @property
    def name(self):
        return type(self).__name__


class Grass(Terrain):
    ANSI_GRASS = "\033[01;38;05;70m"
    
    def __str__(self) -> str:
        return self.ANSI_GRASS + random.choice([' ` ', ' " ', " ' ", ' , ']) + self.ANSI_RESET


class Rock(Terrain):
    ANSI_ROCK = "\033[30m"

    def __str__(self) -> str:
        return self.ANSI_ROCK + random.choice([' ☗ ', ' ⭓ ']) + self.ANSI_RESET


class Tree(Terrain):
    ANSI_TREE = "\033[01;38;05;94m"

    def __str__(self) -> str:
        return self.ANSI_TREE + random.choice([' ║ ', ' │ ']) + self.ANSI_RESET
