import itertools
import random

from bfs import BFS
from terrain import Rock, Tree, Grass
from animals import Herbivore

class SimulationRenderer:
    def __init__(self, simulation) -> None:
        self.simulation = simulation
    
    def render(self):
        pass



class Simulation:
    def __init__(self, board_size_x, board_size_y) -> None:
        self.board_size_x = board_size_x
        self.board_size_y = board_size_y

        self.turns_cnt = 0
        self.terrain_graph = {}
        self.animals_graph = {}
        self.renderer = SimulationRenderer(self)

    def set_objects(self):
        possible_coordinates = (
            itertools.product([x for x in range(self.board_size_x)], 
                              [y for y in range(self.board_size_y)]) )
        
        # животных не должно быть слишком много
        coordinates_for_animals = (random.choices
        (possible_coordinates, 
         random.randint(1, self.board_size_x * self.board_size_y // 2)) )
        
        coordinates_for_terrain = (random.choices
        (possible_coordinates, 
         random.randint(1, self.board_size_x * self.board_size_y)) )


    # def get_neighbor_coordinates(self):
    #     moves = filter(lambda x: isinstance(self.graph[x], Terrain), super().get_neighbor_coordinates())




    


if __name__ == '__main__':


    d = {}
    for i in range(3):
        for j in range(4):
            d[(i, j)] = Rock(i, j, 3, 4)
    d[(2,3)] = Grass(2, 3, 3, 4)
    for i in range(3):
        for j in range(4):
            print(d[(i, j)], end=' ')
        print()

    # print(d[(1, 1)].get_neighbours_coordinates())
    bfs = BFS(d)
    print(bfs.search((0, 0), 'Grass'))

# todo: Движение животных -- если цель найдена, подойти к ней как можно ближе
#       если не найдена -- сделать случайный ход из возможных

# todo: Класс игры. Содержит отдельный словарь для статичных объектов и животных
# Животное не уничтожает объект, по которому ходит, если только это не травоядное
# Правильная отрисовка поля -- животное поверх местности

# споки