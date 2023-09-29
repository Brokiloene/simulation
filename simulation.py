import random
import time

from utils import Coordinate

from entities import Terrain, Rock, Tree, Grass, Animal, Herbivore, Predator

from console_renderer import SimulationConsoleRenderer
from simulation_map import SimulationMap

class Simulation:
    def __init__(self, board_size_row=10, board_size_col=10):
        self.bd_size_row = board_size_row
        self.bd_size_col = board_size_col
        self.bd_area = self.bd_size_row * self.bd_size_col

        self.map = SimulationMap(self.bd_size_row, self.bd_size_col)
        
        self.available_terrain = [Rock, Tree, Grass]
        self.available_animals = [Herbivore, Predator]

        self.turns_cnt = 0
        self.renderer = SimulationConsoleRenderer(self.map)
    
    def init_map_manual(self):
        self.map.instantiate_object(Animal, Coordinate(0, 0), Predator)
        self.map.instantiate_object(Animal, Coordinate(1, 0), Herbivore)
        self.map.instantiate_object(Animal, Coordinate(0, 1), Herbivore)
        self.map.instantiate_object(Animal, Coordinate(1, 1), Herbivore)

        self.map.instantiate_object(Terrain, Coordinate(2, 0), Rock)
        self.map.instantiate_object(Terrain, Coordinate(2, 1), Rock)
        self.map.instantiate_object(Terrain, Coordinate(0, 2), Rock)

        self.map.instantiate_object(Terrain, Coordinate(2, 2), Tree)
        self.map.instantiate_object(Terrain, Coordinate(1, 2), Tree)

        self.map.instantiate_object(Terrain, Coordinate(0, 3), Grass)
        self.map.instantiate_object(Terrain, Coordinate(1, 3), Grass)
        self.map.instantiate_object(Terrain, Coordinate(2, 3), Grass)
        self.map.instantiate_object(Terrain, Coordinate(3, 3), Grass)
        self.map.instantiate_object(Terrain, Coordinate(3, 2), Grass)
        self.map.instantiate_object(Terrain, Coordinate(3, 1), Grass)
        self.map.instantiate_object(Terrain, Coordinate(3, 0), Grass)
        

        self.render()

    def init_map_random(self):
        all_crd = self.map.all_possible_coordinates
        
        # животных не должно быть слишком много
        crd_for_animals = random.choices(all_crd, k=int(self.bd_area ** 0.5))
        
        crd_for_terrain = random.choices(all_crd, k=random.randint(self.bd_area // 2, self.bd_area))
        
        for crd in crd_for_animals:
            animals_to_set = random.choices(self.available_animals, [5, 1], k=len(crd_for_animals))
            for animal_type in animals_to_set:
                self.map.instantiate_object(Animal, crd, animal_type)

        for crd in crd_for_terrain:
            terrain_type = random.choice(self.available_terrain)
            self.map.instantiate_object(Terrain, crd, terrain_type)
            
        self.render()
        

    def render(self):
        self.renderer.render(self.turns_cnt)


    def next_turn(self):
        self.turns_cnt += 1

        for animal in self.map.get_animals:
            if self.map.is_object_exists(animal):
                animal.make_move()
                self.render()

        

if __name__ == '__main__':
    
    sim = Simulation(10, 10)
    sim.init_map_random()

    while True:
        time.sleep(1)
        sim.next_turn()
