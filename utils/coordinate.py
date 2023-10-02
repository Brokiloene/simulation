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
    
    def __hash__(self) -> int:
        return hash(self.values)
    
    def __eq__(self, other) -> bool:
        return self.values == other.values
    
    def __ne__(self, other) -> bool:
        return not(self == other)
    
    def __lt__(self, other):
        return self.row < other.row and self.col < other.col
    
    def __ge__(self, other):
        return self.row >= other.row and self.col >= other.col
    
    def __add__(self, other):
        return Coordinate(self.row + other.row, self.col + other.col)
    
    def __str__(self):
        return str(self.values)
