import random

from entity import Entity



class Terrain(Entity):
    pass


class Grass(Terrain):
    ANSI_GRASS = "\033[01;38;05;70m"
    
    def __str__(self) -> str:
        return self.ANSI_GRASS + random.choice([' ` ', ' " ', " ' ", ' , ']) + self.ANSI_RESET

class EmptyField(Terrain):
    def __str__(self) -> str:
        return '   '

class Rock(Terrain):
    ANSI_ROCK = "\033[30m"

    def __str__(self) -> str:
        return self.ANSI_ROCK + random.choice([' ☗ ', ' ⭓ ']) + self.ANSI_RESET


class Tree(Terrain):
    ANSI_TREE = "\033[01;38;05;94m"

    def __str__(self) -> str:
        return self.ANSI_TREE + random.choice([' ║ ', ' │ ']) + self.ANSI_RESET
