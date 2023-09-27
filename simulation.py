import itertools
import random
import time

from utils.coordinate import Coordinate

from entities.terrain import Rock, Tree, Grass
from entities.animals.herbivore import Herbivore
from entities.animals.predator import Predator

from console_renderer import SimulationConsoleRenderer

class Simulation:
    def __init__(self, board_size_x, board_size_y):
        self.board_size_x = board_size_x
        self.board_size_y = board_size_y
        self.board_size = self.board_size_x * self.board_size_y

        self.terrain_graph = {}
        self.animal_graph = {}
        
        self.available_terrain = [Rock, Tree, Grass]
        self.available_animals = [Herbivore, Predator]

        self.turns_cnt = 0
        self.renderer = SimulationConsoleRenderer(self)
    
    def init_map_manual(self):
        self.animal_graph[Coordinate(2, 2)] = Herbivore(Coordinate(2, 2), Coordinate(self.board_size_x, self.board_size_y), self.terrain_graph, self.animal_graph, 2)
        
        self.terrain_graph[Coordinate(0, 0)] = Grass(Coordinate(0, 0), Coordinate(self.board_size_x, self.board_size_y))
        
        self.terrain_graph[Coordinate(0, 1)] = Rock(Coordinate(0, 1), Coordinate(self.board_size_x, self.board_size_y))
        # self.terrain_graph[Coordinate(1, 0)] = Rock(Coordinate(1, 0), Coordinate(self.board_size_x, self.board_size_y))
        self.terrain_graph[Coordinate(1, 1)] = Rock(Coordinate(1, 1), Coordinate(self.board_size_x, self.board_size_y))
        # self.terrain_graph[Coordinate(2, 1)] = Rock(Coordinate(2, 1), Coordinate(self.board_size_x, self.board_size_y))
        self.terrain_graph[Coordinate(1, 2)] = Rock(Coordinate(1, 2), Coordinate(self.board_size_x, self.board_size_y))
        # self.terrain_graph[Coordinate(2, 0)] = Rock(Coordinate(2, 0), Coordinate(self.board_size_x, self.board_size_y))
        self.terrain_graph[Coordinate(0, 2)] = Rock(Coordinate(0, 2), Coordinate(self.board_size_x, self.board_size_y))


        for crd in self.all_possible_coordinates:
            terrain_args = (crd, Coordinate(self.board_size_x, self.board_size_y))
        
        self.render()

    def init_map_random(self):
        all_crd = self.all_possible_coordinates
        
        # животных не должно быть слишком много
        crd_for_animals = (random.choices
        (all_crd, k=random.randint(1, self.board_size // 4)) )
        
        crd_for_terrain = (random.choices
        (all_crd, k=random.randint(self.board_size // 2, self.board_size)) )
        
        for crd in crd_for_animals:
            animals_to_set = random.choices(self.available_animals, [5, 1], k=len(crd_for_animals))
            for animal in animals_to_set:
                animal_args = (
                                crd, 
                                Coordinate(self.board_size_x, self.board_size_y), 
                                self.terrain_graph, 
                                self.animal_graph
                              )
                self.animal_graph[crd] = animal(*animal_args)

        for crd in crd_for_terrain:
            terrain_args = (
                            crd, 
                            Coordinate(self.board_size_x, self.board_size_y)
                           )
            self.terrain_graph[crd] = random.choice(self.available_terrain)(*terrain_args)

        self.render()
        
    def render(self):
        self.renderer.render(self.turns_cnt)

    def next_turn(self):
        self.turns_cnt += 1

        for animal in list(self.animal_graph.values()):
            if animal in self.animal_graph.values():
                animal.make_move()
                self.render()
        
        # if sum(isinstance(x, Grass) for x in self.terrain_graph) == 0:
        #     self.spawn_grass()
        # if sum(isinstance(x, Herbivore) for x in self.animal_graph) == 0:
        #     self.spawn_herbivore()

    
    @property
    def all_possible_coordinates(self):
        """
        Лист кортежей всех координат всех клеток поля
        """
        return [ Coordinate(*x) for x in itertools.product
            ([*range(self.board_size_x)], [*range(self.board_size_y)]) ]
    
    def spawn_grass(self):
        all_crd = list(filter(lambda x: x not in self.terrain_graph, self.all_possible_coordinates))
        if all_crd:
            Coordinate = random.choice(all_crd)
            self.terrain_graph[Coordinate] = Grass(Coordinate, Coordinate(self.board_size_x, self.board_size_y))

    def spawn_herbivore(self):
        all_crd = list(filter(lambda x: x not in self.animal_graph, self.all_possible_coordinates))
        if all_crd:
            Coordinate = random.choice(all_crd)
            self.animal_graph[Coordinate] = Herbivore(Coordinate, Coordinate(self.board_size_x, self.board_size_y), 2, self.terrain_graph, self.animal_graph)

if __name__ == '__main__':
    
    sim = Simulation(10, 10)
    sim.init_map_random()

    while True:
        time.sleep(1)
        sim.next_turn()

    x=1
