import abc
import random


class Action(abc.ABC):
    def __init__(self, map) -> None:
        self.map = map


    @abc.abstractmethod
    def perform(self):
        pass


    @abc.abstractmethod
    def need_to_perform(self):
        pass
