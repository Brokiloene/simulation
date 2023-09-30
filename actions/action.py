import abc

from simulation_map import SimulationMap


class Action(abc.ABC):
    def __init__(self, map) -> None:
        self.map = map


    @abc.abstractmethod
    def perform(self):
        pass
        

class SpawnGrass(Action):
    def perform(self):
        pass


class SpawnHerbivore(Action):
    pass


class NextTurn(Action):
    pass


class InitMap(Action):
    pass


class MoveAnimal(Action):
    pass
