import random

from actions.action import Action
from entities import Terrain, Grass, Rock, Tree, Animal, Herbivore, Predator


class SpawnAction(Action):
    def need_to_perform(self):
        if self.map.count_instances_of(self.object_to_spawn) != 0:
            return False
        return True


    def perform(self):
        crds_empty = [crd for crd in self.map.all_possible_coordinates if not self.map.is_coordinate_exists_at(crd)]
        crds_for_spawn = random.choices(crds_empty, k=self.spawn_rate)

        for crd in crds_for_spawn:
            self.map.instantiate_object(self.graph, self.object_to_spawn, crd)


class SpawnHerbivore(SpawnAction):
    def __init__(self, map) -> None:
        super().__init__(map)

        self.msg = "SPAWN HERBIVORES"

        self.graph = Animal
        self.object_to_spawn = Herbivore
        self.spawn_rate = max(int(self.map.bd_area * 0.1), 1)


class SpawnPredator(SpawnAction):
    def __init__(self, map) -> None:
        super().__init__(map)

        self.msg = "SPAWN PREDATOR"

        self.graph = Animal
        self.object_to_spawn = Predator
        self.spawn_rate = 1


class SpawnGrass(SpawnAction):
    def __init__(self, map) -> None:
        super().__init__(map)

        self.msg = "SPAWN GRASS"
        
        self.graph = Terrain
        self.object_to_spawn = Grass
        self.spawn_rate = int(self.map.bd_area * 0.2)


class SpawnRock(SpawnAction):
    def __init__(self, map) -> None:
        super().__init__(map)
        
        self.msg = "SPAWN ROCKS"

        self.graph = Terrain
        self.object_to_spawn = Rock
        self.spawn_rate = int(self.map.bd_area * 0.25)


class SpawnTree(SpawnAction):
    def __init__(self, map) -> None:
        super().__init__(map)

        self.msg = "SPAWN TREES"

        self.graph = Terrain
        self.object_to_spawn = Tree
        self.spawn_rate = int(self.map.bd_area * 0.2)
