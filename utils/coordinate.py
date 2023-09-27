class Coordinate:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @classmethod
    def from_coordinate(cls, other):
        return cls(*other.values)
    
    @property
    def values(self):
        return (self.x, self.y)
    
    @property
    def prod(self):
        """
        Возвращает произведение координат
        """
        return self.x * self.y
    
    def __hash__(self) -> int:
        return hash(self.values)
    
    def __eq__(self, other) -> bool:
        return self.values == other.values
    
    def __ne__(self, other) -> bool:
        return not(self == other)
    
    def __lt__(self, other):
        """
        Используется для проверки того, что координаты не выходят за границы карты
        Из-за индексации с 0 неравенство строгое
        """
        return self.x < other.x and self.y < other.y
    
    def __ge__(self, other):
        """
        Используется для проверки того, что координаты не выходят за границы карты
        """
        return self.x >= other.x and self.y >= other.y
    
    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return str(self.values)
    
    def neighbor_coordinates(self, board_size):
        """
        Вернёт список объектов Coordinate -- координаты клеток-соседей self
        """
        neighbor_coordinates = []

        for shift in ((1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)):
            cur = Coordinate(self.x + shift[0], self.y + shift[1])
            if Coordinate(0, 0) <= cur < board_size:   
               neighbor_coordinates.append(cur)

        return neighbor_coordinates

if __name__ == '__main__':
    a1 = Coordinate(0, 0)
    a2 = Coordinate.from_coordinate(a1)
    print(a2.values)