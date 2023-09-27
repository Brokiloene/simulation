import abc


class Entity(abc.ABC):
    def __init__(self, coordinates, board_size) -> None:
        self._sprite = None
        self.coordinates = coordinates
        self.board_size = board_size

    @property
    def sprite(self):
        return self._sprite

