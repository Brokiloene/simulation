import itertools
import random

from bfs import BFS
from terrain import Rock, Tree, Grass
from animals import Herbivore, Predator

class SimulationRenderer:    
    ANSI_BG = "\033[01;48;05;185m"
    ANSI_RESET = "\033[0m"

    def __init__(self, simulation) -> None:
        self.simulation = simulation
    
    def render(self):
        coordinates = self.simulation.all_possible_coordinates
        col_cnt = 0
        row_cnt = 0

        print(' ', end='')
        print(*[x for x in list(map(lambda x: ' ' + str(x) + ' ', range(self.simulation.board_size_y)))], sep='')
        
        print(row_cnt, end='')
        for cord in coordinates:
            if cord in self.simulation.animal_graph:
                print(self.simulation.animal_graph[cord], end='')
            elif cord in self.simulation.terrain_graph:
                print(self.simulation.terrain_graph[cord], end='')
            else:
                print('   ', end='')
            
            col_cnt += 1
            if col_cnt == self.simulation.board_size_y:
                print()
                col_cnt = 0
                row_cnt += 1
                if row_cnt < self.simulation.board_size_x:
                    print(row_cnt, end='')





class Simulation:
    def __init__(self, board_size_x, board_size_y) -> None:
        self.board_size_x = board_size_x
        self.board_size_y = board_size_y
        self.board_size = self.board_size_x * self.board_size_y

        self.turns_cnt = 0
        self.terrain_graph = {}
        self.animal_graph = {}
        self.renderer = SimulationRenderer(self)

        self.available_terrain = [Rock, Tree, Grass]
        self.available_animals = [Herbivore, Predator]

        self.renderer = SimulationRenderer(self)

    def set_objects(self):
        possible_coordinates = self.all_possible_coordinates
        
        # животных не должно быть слишком много
        coordinates_for_animals = (random.choices
        (possible_coordinates, k=random.randint(1, self.board_size // 2)) )
        
        coordinates_for_terrain = (random.choices
        (possible_coordinates, k=random.randint(self.board_size // 2, self.board_size)) )
        
        for cord in coordinates_for_animals:
            animals_to_set = random.choices(self.available_animals, [3, 1], k=len(coordinates_for_animals))
            for animal in animals_to_set:
                speed = random.randint(1, 3)
                animal_args = (*cord, self.board_size_x, self.board_size_y, speed, self.terrain_graph, self.animal_graph)
                self.animal_graph[cord] = animal(*animal_args)

        for cord in coordinates_for_terrain:
            terrain_args = (*cord, self.board_size_x, self.board_size_y)
            self.terrain_graph[cord] = random.choice(self.available_terrain)(*terrain_args)
        
    def render(self):
        self.renderer.render()
    
    @property
    def all_possible_coordinates(self):
        return list(itertools.product([x for x in range(self.board_size_x)], 
                                 [y for y in range(self.board_size_y)]))



    


if __name__ == '__main__':
    sim = Simulation(10, 10)
    sim.set_objects()
    sim.render()
    x=1

# todo: Движение животных -- если цель найдена, подойти к ней как можно ближе
#       если не найдена -- сделать случайный ход из возможных
