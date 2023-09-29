import abc


class Entity(abc.ABC):
    def __init__(self, coordinate) -> None:
        self._sprite = None
        self.crd = coordinate


    @property
    def sprite(self):
        return self._sprite

