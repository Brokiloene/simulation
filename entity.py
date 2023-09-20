import random
import itertools


class Entity:
    """
    Базовый класс. Хранит свои координаты и размеры игровой доски.
    """
    def __init__(self, x, y, board_size_x, board_size_y) -> None:
        self.pos_x = x
        self.pos_y = y
        self.board_size_x = board_size_x
        self.board_size_y = board_size_y

    def is_coordinate_valid(self, cord):
        return 0 <= cord[0] < self.board_size_x and \
               0 <= cord[1] < self.board_size_y
 

    @property
    def neighbor_coordinates(self):
        """
        Вернёт список кортежей -- координаты клеток-соседей self
        """
        neighbor_coordinates = []

        for shift in ((1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1)):
            cur = (self.pos_x + shift[0], self.pos_y + shift[1])
            if self.is_coordinate_valid(cur):   
               neighbor_coordinates.append((self.pos_x + shift[0], self.pos_y + shift[1]))

        return neighbor_coordinates
    
    @property
    def coordinates(self):
        return (self.pos_x, self.pos_y)
    
    def __str__(self) -> str:
        return f"Entity: ({self.pos_x}, {self.pos_y})"
    
    def __repr__(self) -> str:
        return f"Entity({self.pos_x}, {self.pos_y}, {self.board_size_x}, {self.board_size_y})"
