import itertools
import random
import time

from coordinates import Coordinates
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
        for coordinate in coordinates:
            if coordinate in self.simulation.animal_graph:
                print(self.simulation.animal_graph[coordinate], end='')
            elif coordinate in self.simulation.terrain_graph:
                print(self.simulation.terrain_graph[coordinate], end='')
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
    
    def set_test(self):
        self.animal_graph[Coordinates(0, 0)] = Herbivore(Coordinates(0, 0), Coordinates(self.board_size_x, self.board_size_y), 2, self.terrain_graph, self.animal_graph)
        self.animal_graph[Coordinates(9, 0)] = Predator(Coordinates(9, 0), Coordinates(self.board_size_x, self.board_size_y), 3, self.terrain_graph, self.animal_graph)
        
        self.terrain_graph[Coordinates(9, 9)] = Grass(Coordinates(9, 9), Coordinates(self.board_size_x, self.board_size_y))

        for coordinate in self.all_possible_coordinates:
            terrain_args = (
                            coordinate, 
                            Coordinates(self.board_size_x, self.board_size_y)
                           )
        
        self.render()

    def set_random(self):
        possible_coordinates = self.all_possible_coordinates
        
        # животных не должно быть слишком много
        coordinates_for_animals = (random.choices
        (possible_coordinates, k=random.randint(1, self.board_size // 4)) )
        
        coordinates_for_terrain = (random.choices
        (possible_coordinates, k=random.randint(self.board_size // 2, self.board_size)) )
        
        for coordinate in coordinates_for_animals:
            animals_to_set = random.choices(self.available_animals, [5, 1], k=len(coordinates_for_animals))
            for animal in animals_to_set:
                speed = random.randint(1, 3)
                animal_args = (
                                coordinate, 
                                Coordinates(self.board_size_x, self.board_size_y), 
                                speed, 
                                self.terrain_graph, 
                                self.animal_graph
                              )
                self.animal_graph[coordinate] = animal(*animal_args)

        for coordinate in coordinates_for_terrain:
            terrain_args = (
                            coordinate, 
                            Coordinates(self.board_size_x, self.board_size_y)
                           )
            self.terrain_graph[coordinate] = random.choice(self.available_terrain)(*terrain_args)

        self.render()
        
    def render(self):
        self.renderer.render()

    def next_turn(self):
        self.turns_cnt += 1
        print("TURN: ", self.turns_cnt)

        # map(lambda x: x.make_move(), self.animal_graph.values())
        for animal in list(self.animal_graph.values()):
            animal.make_move()
        self.render()
    
    @property
    def all_possible_coordinates(self):
        """
        Лист кортежей всех координат всех клеток поля
        """
        return [ Coordinates(*x) for x in itertools.product
            ([*range(self.board_size_x)], [*range(self.board_size_y)]) ]
        

if __name__ == '__main__':
    
    sim = Simulation(10, 10)
    sim.set_random()
    
    while True:
        time.sleep(1)
        sim.next_turn()

    x=1

# TODO: счетчик животных и хищников
# TODO: спаун травы если ее мало осталось
# TODO: решить проблему с исчезающими хищниками