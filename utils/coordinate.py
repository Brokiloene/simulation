class Coordinate:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

    @classmethod
    def from_coordinate(cls, other):
        return cls(*other.values)
    
    @property
    def values(self):
        return (self.row, self.col)
    
    @property
    def prod(self):
        """
        Возвращает произведение координат
        """
        return self.row * self.col
    
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
        return self.row < other.row and self.col < other.col
    
    def __ge__(self, other):
        """
        Используется для проверки того, что координаты не выходят за границы карты
        """
        return self.row >= other.row and self.col >= other.col
    
    def __add__(self, other):
        return Coordinate(self.row + other.row, self.col + other.col)
    
    def __str__(self):
        return str(self.values)
    

if __name__ == '__main__':
    a1 = Coordinate(0, 0)
    a2 = Coordinate.from_coordinate(a1)
    print(a2.values)