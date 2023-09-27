from entities.animals.animal import Animal
from entities.terrain import Grass
from utils.bfs import Bfs


class Herbivore(Animal):
    def __init__(self, coordinate, board_size, terrain_graph, animal_graph, speed=2) -> None:
        super().__init__(coordinate, board_size, terrain_graph, animal_graph, speed)
        self._sprite = ' H '


    def is_coordinate_free_to_move(self, coordinate):
        is_passable = super().is_coordinate_free_to_move(coordinate)
        if not is_passable or coordinate in self.a_graph:
            return False    
        return True


    def make_move(self):
        if self.crd in self.t_graph and isinstance(self.t_graph[self.crd], Grass):
            del self.t_graph[self.crd]
            # return
        
        path_to_target = Bfs.search(self, Grass, self.t_graph)
        
        if path_to_target:
            move_to = self.find_optimal_coordinate_to_move(path_to_target)
            
            del self.a_graph[self.crd]
            self.a_graph[move_to] = self
            self.crd = move_to
            return
        else:
            self.make_random_move()

