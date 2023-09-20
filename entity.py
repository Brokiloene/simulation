from coordinates import Coordinates


class Entity:
    """
    Базовый класс. Хранит свои координаты и размеры игровой доски.
    """

    ANSI_RESET = "\033[0m"

    def __init__(self, coordinates, board_size) -> None:
        self.coordinates = coordinates
        self.board_size = board_size
    
    @property
    def name(self):
        return type(self).__name__
